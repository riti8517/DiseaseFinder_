from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import pickle
import os
from groq import Groq

# ---------- Load CSV safely ----------
try:
    df = pd.read_csv("symptoms.csv")
    print("✅ symptoms.csv loaded successfully!")
except FileNotFoundError:
    print("❌ ERROR: symptoms.csv not found.")
    df = pd.DataFrame(columns=["Disease"])

# ---------- Build all knowledge statements ----------
statements = []
for _, row in df.iterrows():
    disease = row.get("Disease", None)
    if not disease:
        continue
    symptoms = [str(s) for s in row[1:] if pd.notna(s)]
    if symptoms:
        statements.append(f"If symptoms are {', '.join(symptoms)}, then disease is {disease}.")

print(f"✅ Loaded {len(statements)} disease statements.")
print("Sample:", statements[:5])

# ---------- Helper: limit context length ----------
def limit_context(text: str, max_words: int = 400) -> str:
    words = text.split()
    if len(words) > max_words:
        return " ".join(words[:max_words])
    return text

# ---------- Helper: retrieve relevant context ----------
def get_relevant_context(question: str) -> str:
    q = question.lower()
    relevant = []

    # Priority: if the question mentions a specific disease name, return only rows for that disease.
    # This handles the "Discuss with AI" trigger which says: 'I was predicted to have "Malaria" based on...'
    for disease_name in _DISEASE_TO_JAVA_ID.keys():
        if disease_name.lower() in q:
            for _, row in df.iterrows():
                d = row.get("Disease", None)
                if d and d.lower() == disease_name.lower():
                    syms = [str(s) for s in row[1:] if pd.notna(s)]
                    if syms:
                        relevant.append(f"If symptoms are {', '.join(syms)}, then disease is {d}.")
            if relevant:
                return limit_context("\n".join(relevant))

    # Fallback: symptom keyword matching
    for _, row in df.iterrows():
        disease = row.get("Disease", None)
        if not disease:
            continue
        symptoms = [str(s).lower() for s in row[1:] if pd.notna(s)]
        if any(symptom in q for symptom in symptoms):
            relevant.append(f"If symptoms are {', '.join(symptoms)}, then disease is {disease}.")
    if not relevant:
        relevant = statements[:5]
    else:
        relevant = relevant[:10]
    return limit_context("\n".join(relevant))

# ---------- LLM template ----------
SYSTEM_PROMPT = "You are a medical assistant. Answer in 2-3 sentences max. If the user mentions a specific predicted disease, explain that disease, its causes, and what to do next. Do not suggest a different disease. If unsure, suggest seeing a doctor."

# ---------- Disease name → Java numeric ID mapping ----------
# Must match Java's CacheManager.initDisease() exactly.
_DISEASE_TO_JAVA_ID = {
    "Fungal infection": 0.0,
    "Allergy": 1.0,
    "GERD": 2.0,
    "Chronic cholestasis": 3.0,
    "Drug Reaction": 4.0,
    "Peptic ulcer diseae": 5.0,
    "AIDS": 6.0,
    "Diabetes": 7.0,
    "Gastroenteritis": 8.0,
    "Bronchial Asthma": 9.0,
    "Hypertension": 10.0,
    "Migraine": 11.0,
    "Cervical spondylosis": 12.0,
    "Paralysis (brain hemorrhage)": 13.0,
    "Jaundice": 14.0,
    "Malaria": 15.0,
    "Chicken pox": 16.0,
    "Dengue": 17.0,
    "Typhoid": 18.0,
    "hepatitis A": 19.0,
    "Hepatitis B": 20.0,
    "Hepatitis C": 21.0,
    "Hepatitis D": 22.0,
    "Hepatitis E": 23.0,
    "Alcoholic hepatitis": 24.0,
    "Tuberculosis": 25.0,
    "Common Cold": 26.0,
    "Pneumonia": 27.0,
    "Dimorphic hemmorhoids(piles)": 28.0,
    "Heart attack": 29.0,
    "Varicose veins": 30.0,
    "Hypothyroidism": 31.0,
    "Hyperthyroidism": 32.0,
    "Hypoglycemia": 33.0,
    "Osteoarthristis": 34.0,
    "Arthritis": 35.0,
    "(vertigo) Paroymsal  Positional Vertigo": 36.0,
    "Acne": 37.0,
    "Urinary tract infection": 38.0,
    "Psoriasis": 39.0,
    "Impetigo": 40.0,
}
# Build a lowercase lookup to handle case mismatches from training data
_DISEASE_LOWER_LOOKUP = {k.lower(): v for k, v in _DISEASE_TO_JAVA_ID.items()}

def disease_name_to_java_id(name: str) -> float:
    """Convert a disease name string to Java's numeric disease ID."""
    if name in _DISEASE_TO_JAVA_ID:
        return _DISEASE_TO_JAVA_ID[name]
    lower = name.lower().strip()
    if lower in _DISEASE_LOWER_LOOKUP:
        return _DISEASE_LOWER_LOOKUP[lower]
    print(f"⚠️ Unknown disease name: '{name}' — defaulting to 0.0")
    return 0.0

# ---------- Load ML model ----------
# Model is trained with Java's symptom ordering — no remapping needed.
_LOCAL_MODEL_PATH = "/home/titi/workingdir3/DiseaseFinder_/model_serving/diseaseFinder_java_order.pkl"
_EC2_MODEL_PATH = "/home/ubuntu/DiseaseFinder_/model_serving/diseaseFinder_java_order.pkl"
_ENV_MODEL_PATH = os.environ.get("MODEL_PATH", "")

if _ENV_MODEL_PATH and os.path.exists(_ENV_MODEL_PATH):
    MODEL_PATH = _ENV_MODEL_PATH
elif os.path.exists(_LOCAL_MODEL_PATH):
    MODEL_PATH = _LOCAL_MODEL_PATH
elif os.path.exists(_EC2_MODEL_PATH):
    MODEL_PATH = _EC2_MODEL_PATH
else:
    MODEL_PATH = _LOCAL_MODEL_PATH  # will fail gracefully below

MODEL_FEATURES = 131  # model was trained on 131 features

try:
    with open(MODEL_PATH, "rb") as f:
        _classifier = pickle.load(f)
    print("✅ ML model loaded successfully!")
except Exception as e:
    print("❌ ML model load failed:", e)
    _classifier = None

# ---------- Groq LLM Setup ----------
_groq_client = None
try:
    _api_key = os.environ.get("GROQ_API_KEY", "")
    if not _api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")
    _groq_client = Groq(api_key=_api_key)
    print("✅ Groq client initialized successfully!")
except Exception as e:
    print("❌ Groq setup failed:", e)

# ---------- FastAPI setup ----------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Pydantic models ----------
class ChatRequest(BaseModel):
    history: list[dict] = []
    question: str

class ChatResponse(BaseModel):
    answer: str

# ---------- Chat endpoint ----------
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    user_text = req.question
    print("🗣️ User:", user_text)

    if not _groq_client:
        return {"answer": "Error: LLM model not available. Please set GROQ_API_KEY."}

    try:
        context_text = get_relevant_context(user_text)
        print(f"📘 Context size: {len(context_text.split())} words")

        user_message = f"Knowledge:\n{context_text}\n\nUser: {user_text}"

        response = _groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            max_tokens=150,
        )
        answer = response.choices[0].message.content.strip()

        print("🤖 Answer:", answer)
        return {"answer": answer}

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"answer": f"Sorry, something went wrong: {str(e)}"}


# ---------- Predict endpoint (called by Java backend) ----------
@app.get("/predict")
def predict_disease(data: str = Query(...)):
    if not _classifier:
        return {"error": "Model not loaded"}
    try:
        int_arr = [int(x) for x in data.split(",")]
        # Pad or truncate to match model's expected feature count
        if len(int_arr) < MODEL_FEATURES:
            int_arr += [0] * (MODEL_FEATURES - len(int_arr))
        else:
            int_arr = int_arr[:MODEL_FEATURES]
        prediction = _classifier.predict([int_arr])
        predicted_class = prediction[0]
        java_id = disease_name_to_java_id(str(predicted_class))
        print(f"🔮 Prediction: {predicted_class} → Java ID: {java_id}")
        return {"prediction": [java_id]}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

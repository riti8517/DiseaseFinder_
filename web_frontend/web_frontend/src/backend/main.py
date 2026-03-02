from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import numpy as np
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
SYSTEM_PROMPT = "You are a medical assistant. Answer in 2-3 sentences max. Name the most likely disease and briefly explain. If unsure, suggest seeing a doctor."

# ---------- Load ML model ----------
# Support both local dev path and EC2 path
_LOCAL_MODEL_PATH = "/home/titi/workingdir3/DiseaseFinder_/model_serving/diseaseFinder_neural_network_2025.pkl"
_EC2_MODEL_PATH = "/home/ubuntu/DiseaseFinder_/model_serving/diseaseFinder_neural_network_2025.pkl"
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
        column_names = [f"Symptom_{i+1}" for i in range(MODEL_FEATURES)]
        df_input = pd.DataFrame([int_arr], columns=column_names)
        prediction = _classifier.predict(df_input)
        predicted_class = int(np.argmax(np.array(prediction)))
        print(f"🔮 Prediction: class {predicted_class}")
        return {"prediction": [predicted_class]}
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

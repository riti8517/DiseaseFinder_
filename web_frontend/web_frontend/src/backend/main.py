from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd

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
TEMPLATE = """You are a medical assistant. Answer in 2-3 sentences max.

Knowledge:
{context}

User: {question}

Name the most likely disease and briefly explain. If unsure, suggest seeing a doctor."""

# ---------- LLM Setup ----------
try:
    # Change model name if you fine-tune later, e.g. "medical-assistant"
    _llm = OllamaLLM(model="llama3", num_predict=150)
    _prompt = ChatPromptTemplate.from_template(TEMPLATE)
    _chain = _prompt | _llm
    print("✅ LLM model loaded successfully!")
except Exception as e:
    print("❌ LLM setup failed:", e)
    _chain = None

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

    # Check model
    if not _chain:
        return {"answer": "Error: LLM model not available."}

    try:
        # Build relevant context dynamically
        context_text = get_relevant_context(user_text)
        print(f"📘 Context size: {len(context_text.split())} words")

        # Query model
        raw_answer = _chain.invoke({"context": context_text, "question": user_text})
        answer = str(raw_answer).strip()

        print("🤖 Answer:", answer)
        return {"answer": answer}

    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"answer": f"Sorry, something went wrong: {str(e)}"}


# ---------- Fine-tuning Integration (optional) ----------
"""
💡 Fine-tuning Steps (for later):

1. Collect training examples in JSONL:
   {"prompt": "Symptoms: fever, cough", "response": "Likely flu or COVID."}

2. Fine-tune your model using Ollama or OpenAI API.
   For Ollama:
     - Create a Modelfile with:
         FROM llama3
         PARAMETER temperature 0.7
         TEMPLATE "You are a concise medical assistant..."
     - Then run:
         ollama create medical-assistant -f Modelfile

3. Update this line to use your fine-tuned model:
     _llm = OllamaLLM(model="medical-assistant")
"""

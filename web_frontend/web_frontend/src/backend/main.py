from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

TEMPLATE = """
You are a helpful, friendly, and knowledgeable AI medical assistant.
...
"""

_llm    = OllamaLLM(model="llama3")             
_prompt = ChatPromptTemplate.from_template(TEMPLATE)
_chain  = _prompt | _llm

app = FastAPI()

# CORS middleware added here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domain if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    history: list[dict]
    question: str

class ChatResponse(BaseModel):
    answer: str

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    context_text = "\n".join(
        f"{m['role'].capitalize()}: {m['content']}" for m in req.history
    )
    answer = _chain.invoke({"context": context_text, "question": req.question}).strip()
    return {"answer": answer}

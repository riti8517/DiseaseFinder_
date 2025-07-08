# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

TEMPLATE = """
You are a helpful, friendly, and knowledgeable AI assistant.

Instructions:
- Respond concisely and clearly.
- If the question is unclear, ask for clarification.
- Refer to past conversation if relevant.
- If asked about a disease answer clearly to understand give definition on disease
  and talk about what you can do to help yourself

Here is the conversation history:
{context}

User's question:
{question}

Answer:
"""

_llm    = OllamaLLM(model="llama3")             
_prompt = ChatPromptTemplate.from_template(TEMPLATE)
_chain  = _prompt | _llm


app = FastAPI()

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

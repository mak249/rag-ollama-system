from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.rag import rag_query



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React frontend URL
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/query")
def query(data: dict):
    question = data.get("question", "")
    if not question:
        return {"error": "No question provided"}
    answer = rag_query(question)
    return {"answer": answer}

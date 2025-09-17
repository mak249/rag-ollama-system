
from fastapi import FastAPI
from pydantic import BaseModel
from backend.rag import query_rag  # your function to query RAG

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "RAG API is running"}

@app.post("/ask")
def ask_question(q: Question):
    answer = query_rag(q.question)
    return {"answer": answer}

# Only put server logic here if running directly, not ingestion
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)

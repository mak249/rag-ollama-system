
import os
import ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chroma_db")

def rag_query(question: str) -> str:
    embedding = OllamaEmbeddings(model=os.getenv("EMBED_MODEL", "nomic-embed-text"))
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embedding)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    docs = retriever.get_relevant_documents(question)

    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = f"Answer the question based on context:\n\n{context}\n\nQuestion: {question}"

    try:
        response = ollama.chat(
            model=os.getenv("CHAT_MODEL", "llama3"),
            messages=[{"role": "user", "content": prompt}],
            options={"timeout": 30, "num_predict": 128}
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {e}\nMake sure Ollama is running: ollama serve"

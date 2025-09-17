

import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")
DB_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")

def ingest_documents():
    docs = []
    if not os.path.isdir(DOCS_DIR):
        print(f"⚠️  Docs folder not found at {DOCS_DIR}")
        return

    for file in os.listdir(DOCS_DIR):
        path = os.path.join(DOCS_DIR, file)
        if file.lower().endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif file.lower().endswith(".txt") or file.lower().endswith(".text"):
            docs.extend(TextLoader(path).load())

    if not docs:
        print("⚠️  No documents found to ingest.")
        return

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embedding = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(chunks, embedding, persist_directory=DB_DIR)
    vectorstore.persist()

    print(f"✅ Ingested {len(chunks)} chunks into {DB_DIR}")

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from app.core.config import settings
import os

def get_vector_store():
    if not settings.GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is not set in environment variables")
        
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004", # Using a standard embedding model
        google_api_key=settings.GOOGLE_API_KEY
    )
    
    vector_store = Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIRECTORY,
        embedding_function=embeddings,
        collection_name="rag_collection"
    )
    
    return vector_store

def add_documents_to_store(documents):
    vector_store = get_vector_store()
    vector_store.add_documents(documents)
    # Chroma automatically persists in newer versions, but we can't hurt ensuring it if method exists
    # vector_store.persist() # Deprecated in newer Chroma, but let's check if needed. usually auto-persists.
    return True

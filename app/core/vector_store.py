from langchain_community.vectorstores import Chroma
from app.core.config import settings
from app.core.llm_factory import get_embeddings


def get_vector_store():
    embeddings = get_embeddings()

    vector_store = Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIRECTORY,
        embedding_function=embeddings,
        collection_name="rag_collection"
    )

    return vector_store

def add_documents_to_store(documents):
    vector_store = get_vector_store()
    vector_store.add_documents(documents)
    return True

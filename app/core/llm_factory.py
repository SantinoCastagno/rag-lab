from langchain_core.language_models import BaseChatModel
from langchain_core.embeddings import Embeddings
from app.core.config import settings


def get_llm() -> BaseChatModel:
    if settings.LLM_PROVIDER == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL_NAME,
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=settings.LLM_TEMPERATURE,
        )
    # ollama
    from langchain_ollama import ChatOllama
    return ChatOllama(
        model=settings.OLLAMA_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
        temperature=settings.LLM_TEMPERATURE,
    )


def get_embeddings() -> Embeddings:
    if settings.LLM_PROVIDER == "gemini":
        from langchain_google_genai import GoogleGenerativeAIEmbeddings
        return GoogleGenerativeAIEmbeddings(
            model=settings.GEMINI_EMBEDDINGS_MODEL,
            google_api_key=settings.GOOGLE_API_KEY,
        )
    # ollama
    from langchain_ollama import OllamaEmbeddings
    return OllamaEmbeddings(
        model=settings.OLLAMA_EMBEDDINGS_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
    )

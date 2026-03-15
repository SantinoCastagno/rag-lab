from typing import Literal
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Provider selection
    LLM_PROVIDER: Literal["gemini", "ollama"] = "gemini"

    # Google Gemini
    GOOGLE_API_KEY: str | None = None
    GEMINI_MODEL_NAME: str = "gemini-2.5-flash-lite"
    GEMINI_EMBEDDINGS_MODEL: str = "models/text-embedding-004"

    # Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "mistral"
    OLLAMA_EMBEDDINGS_MODEL: str = "nomic-embed-text"

    # Shared
    CHROMA_PERSIST_DIRECTORY: str = "./data/chroma_db"
    PHOENIX_PROJECT_NAME: str = "rag-mvp"
    RETRIEVER_K: int = 5
    LLM_TEMPERATURE: float = 0.7
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    @model_validator(mode="after")
    def validate_provider_config(self):
        if self.LLM_PROVIDER == "gemini" and not self.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY es requerido cuando LLM_PROVIDER=gemini")
        return self


settings = Settings()

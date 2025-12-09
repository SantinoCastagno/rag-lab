from fastapi import FastAPI
from app.api import routes
from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor
from app.core.config import settings

app = FastAPI(title="Basic RAG API")

# Initialize Phoenix and OpenTelemetry
# This registers the tracer provider and configures it to send traces to Phoenix
tracer_provider = register(project_name=settings.PHOENIX_PROJECT_NAME)
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

app.include_router(routes.router)

@app.get("/")
async def root():
    return {"message": "Basic RAG API with Gemini 2.5 Flash-Lite"}

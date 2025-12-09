from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.core.ingestion import process_file
from app.core.rag_chain import get_rag_chain

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]

@router.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".md")):
        raise HTTPException(status_code=400, detail="Only PDF and Markdown files are supported")
    
    try:
        content = await file.read()
        num_chunks = process_file(content, file.filename)
        return {"message": f"Successfully ingested {file.filename}", "chunks": num_chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        chain = get_rag_chain()
        result = chain.invoke({"query": request.question})
        
        answer = result.get("result", "")
        source_docs = result.get("source_documents", [])
        sources = [doc.metadata.get("source", "unknown") for doc in source_docs]
        
        # Deduplicate sources
        sources = list(set(sources))
        
        return ChatResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

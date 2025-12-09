# Basic RAG with Gemini 2.5 Flash-Lite

This project is a basic RAG (Retrieval Augmented Generation) system using:
- **LLM:** Gemini 2.5 Flash-Lite
- **Embeddings:** Google Generative AI Embeddings
- **Vector Store:** ChromaDB
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Tracing/Eval:** Arize Phoenix

## Setup

1. **Install Dependencies:**
   ```bash
   poetry install
   ```

2. **Environment Variables:**
   Copy `.env.example` (or just use `.env` created) and set your `GOOGLE_API_KEY`.
   ```bash
   cp .env .env.local
   # Edit .env.local with your API Key
   ```

## Running the Application

You need to run the Phoenix server, the FastAPI backend, and the Streamlit frontend.

### 1. Start Arize Phoenix (Optional but recommended for tracing)
```bash
poetry run python -m phoenix.server.main serve
```
*Access Phoenix UI at http://localhost:6006*

### 2. Start Backend (FastAPI)
```bash
poetry run uvicorn app.api.main:app --reload --port 8000
```
*API docs at http://localhost:8000/docs*

### 3. Start Frontend (Streamlit)
```bash
poetry run streamlit run app/ui/app.py
```
*Access Chatbot at http://localhost:8501*

## Usage
1. Open the Streamlit app.
2. Upload a PDF or Markdown file via the sidebar.
3. Click "Ingest File".
4. Ask questions in the chat.

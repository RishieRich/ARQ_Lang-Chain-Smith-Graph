# agents/ingestion_agent.py
# ─────────────────────────────────────────────────────────────
# Ingestion Agent — first agent in the pipeline.
# Responsibilities:
#   1. Detect file type
#   2. Load file using the correct LangChain loader
#   3. Extract raw text from all pages/sheets
#   4. Split text into chunks for the analysis agent
#   5. Write results to shared state
# ─────────────────────────────────────────────────────────────


from langchain_community.document_loaders import (
    PyPDFLoader,
    CSVLoader,
    Docx2txtLoader,
    TextLoader,
    UnstructuredExcelLoader
)

from langchain.text_splitter import RecursiveCharacterTextSplitter


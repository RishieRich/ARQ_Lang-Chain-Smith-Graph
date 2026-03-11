# config.py
# ─────────────────────────────────────────────────────────────
# Central configuration for the entire insight-agent system.
# Every agent imports settings from here.
# Nothing is hardcoded anywhere else in the codebase.
# Date : 12 March 2026 
# Author : Rishikesh Pote
# ─────────────────────────────────────────────────────────────


import os 
from pathlib import Path
from dotenv import load_dotenv

# ── Load .env file ─────────────────────────────────────────
# This reads your .env file and loads all keys into
# environment variables so os.getenv() can access them.

load_dotenv()

GROQ_API_LEU = os.getenv("GROQ_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")


# ── LLM Settings ───────────────────────────────────────────
# The model we use for all LLM calls via Groq.
# llama-3.3-70b-versatile = best free model on Groq as of Feb 2026.
LLM_MODEL = "llama-3.3-70b-versatile"

# Temperature controls creativity vs accuracy.
# 0.1 = very factual, deterministic (good for document analysis)
# 1.0 = creative, varied (good for writing/brainstorming)

LLM_TEMPERATURE = 0.1

# Max tokens the LLM can return in a single response
LLM_MAX_TOKENS = 4096

# ── Document Chunking ──────────────────────────────────────
# When we load a large document, we split it into chunks
# so the LLM can process it piece by piece.
#
# CHUNK_SIZE = how many characters per chunk
# CHUNK_OVERLAP = how many characters overlap between chunks
#   (overlap preserves context at chunk boundaries)
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200

# ── Paths ──────────────────────────────────────────────────
# BASE_DIR = the root folder of this project (where config.py lives)
BASE_DIR = Path(__file__).parent 

# Where the final Word documents get saved
OUTPUT_DIR = BASE_DIR / "output"

# Where you drop test files (PDFs, Excel, CSV, Word)

SAMPLE_DIR = BASE_DIR / "sample_docs"

# Create these folders if they don't exist yet
OUTPUT_DIR.mkdir(exist_ok=True)
SAMPLE_DIR.mkdir(exist_ok=True)

# ── Quality Gate ───────────────────────────────────────────
# The analysis agent must extract at least this many insights.
# If it finds fewer, the supervisor will flag it as low quality.
MIN_INSIGHTS_REQUIRED = 3

SUPPORTED_EXTENSIONS = [".pdf",".xlsx",".xls",".csv",".docx",".txt"]    
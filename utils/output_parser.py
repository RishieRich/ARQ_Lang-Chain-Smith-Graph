# utils/output_parser.py
# ─────────────────────────────────────────────────────────────
# Handles structured output parsing for all agents.
# Uses Pydantic models + LangChain's with_structured_output()
# to force the LLM to return clean, typed Python objects.
# ─────────────────────────────────────────────────────────────

from pydantic import BaseModel, Field
from typing import List


# Analysis Output Schema
# This is the exact shape we demand from the analysis LLM call.
# Pydantic validates every field - wrong type = automatic error.
# Field () lets us add description so the LLM understands 
# exactly what to put in each field.

class InsightOutput(BaseModel):
    """
    Structured output from the analysis agent.
    Langchain forces the LLM to return exactly this shape.
    """
    
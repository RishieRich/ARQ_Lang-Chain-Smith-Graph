# graph/state.py
# ─────────────────────────────────────────────────────────────
# Defines the shared state object passed between all agents.
# Think of this as the "whiteboard" every agent reads & writes.
# LangGraph passes this state from node to node automatically.
# ─────────────────────────────────────────────────────────────

from typing import TypedDict, List, Optional 

class AgentState(TypedDict):
    # ── Set by user at the start ───────────────────────────
    # The full path to the file the user wants to analyze
    file_path: str

    # ── Written by Ingestion Agent ─────────────────────────
    # The full raw text extracted from the document
    raw_text : str

    # List of text chunks (raw_text split into smaller pieces)
    # Each chunk is a string the LLM can process in one call
    chunks : List[str]

    # Metadata about the file (name, type, size, page count etc)
    # We use dict so it can hold any key-value pairs
    file_metadata : dict 

    # ── Written by Analysis Agent ──────────────────────────
    # List of insight strings extracted by the LLM
    insights : List[str]

    # Short summary of the entire document (1-2 paragraphs)
    summary : str

    # Key themes found in the document
    themes : List[str]

    # ── Written by Writer Agent ────────────────────────────
    # Full path to the generated Word document
    output_path : str

    # ── Written by Supervisor ──────────────────────────────
    # Which agent should run next
    next_agent : str

    # If something goes wrong, the error message goes here
    error: Optional[str]

    # Track which agents have completed (for debugging)
    completed_steps : List[str]
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

# graph/state.py
from typing import TypedDict, List, Optional
from pydantic import BaseModel


class DocumentInsights(BaseModel):
    """Structured output the analysis agent must return."""
    summary: str
    insights: List[str]
    themes: List[str]
    key_facts: List[str]
    confidence_score: float


class AgentState(TypedDict):

    # ── Input ──────────────────────────────────────────────
    file_path: str

    # ── Ingestion Agent ────────────────────────────────────
    raw_text: str
    chunks: List[str]
    file_metadata: dict

    # ── Analysis Agent ─────────────────────────────────────
    insights_data: Optional[dict]

    # ── Evaluation Agent ───────────────────────────────────
    eval_score: Optional[float]
    eval_feedback: Optional[str]
    retry_count: int

    # ── Writer Agent ───────────────────────────────────────
    output_path: Optional[str]

    # ── Supervisor ─────────────────────────────────────────
    next_agent: str
    error: Optional[str]
    completed_steps: List[str]

    # ── Human in the loop ──────────────────────────────────
    awaiting_human_review: bool
    human_approved: Optional[bool]
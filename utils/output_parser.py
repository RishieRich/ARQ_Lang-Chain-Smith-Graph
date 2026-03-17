# utils/output_parser.py
# ─────────────────────────────────────────────────────────────
# Handles structured output parsing for all agents.
# Uses Pydantic models + LangChain's with_structured_output()
# to force the LLM to return clean, typed Python objects.
# ─────────────────────────────────────────────────────────────

from pydantic import BaseModel, Field
from typing import List


# ── Analysis Output Schema ─────────────────────────────────
# This is the exact shape we demand from the analysis LLM call.
# Pydantic validates every field — wrong type = automatic error.
# Field() lets us add a description so the LLM understands
# exactly what to put in each field.

class InsightOutput(BaseModel):
    """
    Structured output from the analysis agent.
    LangChain forces the LLM to return exactly this shape.
    """

    summary: str = Field(
        description="A 2-3 paragraph summary of the entire document"
    )

    insights: List[str] = Field(
        description="List of key insights. Each insight is one clear sentence."
    )

    themes: List[str] = Field(
        description="List of main themes or topics found in the document"
    )

    key_facts: List[str] = Field(
        description="Important numbers, dates, names, or figures from the document"
    )

    confidence_score: float = Field(
        description="Your confidence in this analysis from 0.0 to 1.0. "
                    "1.0 means the document was clear and complete. "
                    "0.5 means the document was vague or incomplete."
    )


# ── Evaluation Output Schema ───────────────────────────────
# Shape we demand from the evaluation LLM call.
# Evaluation agent uses this to score analysis quality.

class EvaluationOutput(BaseModel):
    """
    Structured output from the evaluation agent.
    Contains a quality score and detailed feedback.
    """

    score: float = Field(
        description="Overall quality score from 0.0 to 1.0. "
                    "Above 0.7 means output is ready for the client."
    )

    faithfulness: float = Field(
        description="Are all insights grounded in the source document? 0.0 to 1.0"
    )

    completeness: float = Field(
        description="Are the most important points covered? 0.0 to 1.0"
    )

    clarity: float = Field(
        description="Is the summary clear and well structured? 0.0 to 1.0"
    )

    feedback: str = Field(
        description="Specific explanation of what is good and what is missing or wrong"
    )

    passed: bool = Field(
        description="True if score >= 0.7 and output is ready for client. False if retry needed."
    )


# ── Helper: convert Pydantic model to dict ─────────────────
# AgentState stores insights_data as a plain dict
# (TypedDict cant hold Pydantic objects directly).
# This helper converts cleanly.

def insight_to_dict(insight: InsightOutput) -> dict:
    """Converts InsightOutput Pydantic model to plain dict for state storage."""
    return {
        "summary": insight.summary,
        "insights": insight.insights,
        "themes": insight.themes,
        "key_facts": insight.key_facts,
        "confidence_score": insight.confidence_score
    }


def eval_to_dict(evaluation: EvaluationOutput) -> dict:
    """Converts EvaluationOutput Pydantic model to plain dict for state storage."""
    return {
        "score": evaluation.score,
        "faithfulness": evaluation.faithfulness,
        "completeness": evaluation.completeness,
        "clarity": evaluation.clarity,
        "feedback": evaluation.feedback,
        "passed": evaluation.passed
    }
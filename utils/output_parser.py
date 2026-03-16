# utils/output_parser.py
# ─────────────────────────────────────────────────────────────
# Handles structured output parsing for all agents.
# Uses Pydantic models + LangChain's with_structured_output()
# to force the LLM to return clean, typed Python objects.
# ─────────────────────────────────────────────────────────────


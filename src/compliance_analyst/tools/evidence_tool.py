"""Tool to get the evidence to look for in each requirement (agent 1)."""

from agents import function_tool
from .evidence_map import EVIDENCE_REQUIREMENTS


@function_tool
def get_required_evidence(requirement_id: str) -> list[dict] | str:
    """Return the evidence checklist for one requirement.

    Args:
        requirement_id: A requirement ID such as "AI-001".
    """
    items = EVIDENCE_REQUIREMENTS.get(requirement_id)
    if items is None:
        valid = ", ".join(EVIDENCE_REQUIREMENTS)
        return f"Unknown requirement_id '{requirement_id}'. Valid IDs: {valid}"
    return items
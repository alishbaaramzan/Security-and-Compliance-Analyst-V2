"""Pydantic models for the output of the compliance analyst agents."""

from typing import Literal

from pydantic import BaseModel

Verdict = Literal["PASS", "FAIL", "UNKNOWN"]
OverallStatus = Literal["PASS", "REVIEW_REQUIRED"]


class RequirementVerdict(BaseModel):
    """Agent 1's assessment of a single requirement."""

    requirement_id: str
    verdict: Verdict
    evidence: str
    recommended_action: str


class MappingResult(BaseModel):
    """Agent 1's full output: every requirement, assessed once."""

    requirement_verdicts: list[RequirementVerdict]


class RiskAssessment(BaseModel):
    """Agent 2's output: reasoning across all verdicts."""

    overall_status: OverallStatus
    gaps: list[str]
    risks: list[str]
    next_steps: list[str]


class FinalReport(BaseModel):
    """The assembled report returned to the caller."""

    requirement_verdicts: list[RequirementVerdict]
    overall_status: OverallStatus
    gaps: list[str]
    risks: list[str]
    next_steps: list[str]

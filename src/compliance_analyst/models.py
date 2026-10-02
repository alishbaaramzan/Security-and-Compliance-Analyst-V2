"""
Pydantic schemas shared across agents, tools, and guardrails.

The Agents SDK uses these for structured outputs (Agent(..., output_type=X))
and for guardrail payloads, so get these right first -- everything else
is built around them.

Hints on what you'll likely need:

UseCase
    The normalized, JSON-shaped representation of a submitted AI use case
    (whatever fields the text_to_json tool / direct JSON submission produce).
    Consider: name, description, data_processed, data_sensitivity,
    ai_provider, business_owner, human_oversight, logging_monitoring,
    access_controls, third_party_security_assessment, intended_use,
    limitations, risk_level, additional_review. Decide which are required
    vs optional -- missing fields are exactly what should drive UNKNOWN
    verdicts downstream, not validation errors.

Verdict
    Literal["PASS", "FAIL", "UNKNOWN"]

RequirementVerdict  (one row of Agent 1's output)
    - requirement_id: str
    - verdict: Verdict
    - evidence: str          (what evidence was found / cited, or why none)
    - recommended_action: str

MappingResult  (Agent 1's full structured output)
    - requirement_verdicts: list[RequirementVerdict]
    (keep agent 1 focused on mapping only -- no risks/gaps here, that's
    agent 2's job)

RiskAssessment  (Agent 2's structured output)
    - gaps: list[str]
    - risks: list[str]
    - next_steps: list[str]
    - overall_status: Literal[...] (e.g. "PASS", "REVIEW_REQUIRED") --
      decide the rule for deriving this (e.g. any FAIL/UNKNOWN -> review)

FinalReport  (what main.py assembles and returns to the caller)
    - requirement_verdicts: list[RequirementVerdict]
    - gaps / risks / next_steps / overall_status (from RiskAssessment)

Guardrail payloads
    - Agents SDK guardrails return a GuardrailFunctionOutput wrapping
      output_info of whatever shape you want. A small Pydantic model for
      "why did this guardrail trip" (reason: str, tripwire_triggered: bool)
      keeps that consistent across input/output guardrails.
"""

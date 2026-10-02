"""
Agent 2: Risk Reasoner

Responsibility: take Agent 1's per-requirement verdicts (MappingResult) and
reason across all of them to produce the overall picture -- gaps, risks,
next steps, and an overall status.

Hints:
- This agent likely needs no tools at all -- its only input is Agent 1's
  structured output, not the raw use case or the requirements catalog.
  Keep it a pure reasoning step if you can; only give it tools back onto
  the use case/requirements if you find it actually needs to re-check
  something.
- Build with:
    Agent(
        name="risk_reasoner",
        instructions=...,
        output_type=RiskAssessment,
        output_guardrails=[...],
    )
- Instructions should cover:
    - every FAIL and UNKNOWN is a gap that must be surfaced, not smoothed
      over;
    - risks should be concrete (tie back to which requirement(s) drove
      them), not generic boilerplate;
    - next_steps should be actionable and ideally ordered by priority;
    - define explicitly how overall_status is derived (e.g. any
      FAIL/UNKNOWN -> "REVIEW_REQUIRED", all PASS -> "PASS") so the model
      isn't guessing the policy.
- Wire the two agents together in main.py: run mapper_agent first, feed
  its MappingResult (as text/JSON) as the input to risk_reasoner, then
  assemble FinalReport from both outputs. A handoff isn't the right tool
  here since this is a strict sequential pipeline, not a dynamic routing
  decision.
"""

"""Output guardrail: every requirement must be assessed."""

from agents import GuardrailFunctionOutput, RunContextWrapper, output_guardrail

from ..models import MappingResult
from ..tools.requirements_data import REQUIREMENTS


@output_guardrail
def check_mapping_completeness(
    ctx: RunContextWrapper,
    agent,
    agent_output: MappingResult,
) -> GuardrailFunctionOutput:
    expected_ids = {r["id"] for r in REQUIREMENTS}
    actual_ids = {v.requirement_id for v in agent_output.requirement_verdicts}
    missing = expected_ids - actual_ids

    return GuardrailFunctionOutput(
        output_info=f"missing={missing}" if missing else "ok",
        tripwire_triggered=bool(missing),
    )

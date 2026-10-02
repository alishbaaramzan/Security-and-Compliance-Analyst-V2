"""Input guardrail: reject empty use case submissions."""

from agents import GuardrailFunctionOutput, RunContextWrapper, input_guardrail


@input_guardrail
def check_use_case_input(
    ctx: RunContextWrapper,
    agent,
    input: str,
) -> GuardrailFunctionOutput:
    is_empty = not str(input).strip()
    return GuardrailFunctionOutput(
        output_info="empty input" if is_empty else "ok",
        tripwire_triggered=is_empty,
    )

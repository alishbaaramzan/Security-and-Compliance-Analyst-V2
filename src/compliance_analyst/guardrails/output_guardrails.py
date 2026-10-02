"""
Output guardrail(s) -- run against the agents' structured output before
it's returned to the caller.

What this should actually guard against:
- Agent 1 (mapper): every requirement in the catalog appears exactly once
  in requirement_verdicts (no duplicates, nothing missing) -- the same
  invariant the old project enforced by hand in _validate_assessment.
  This is really an application-level check and can mostly be plain
  Python, but wiring it as an @output_guardrail keeps the "reject bad
  output" policy in one consistent place alongside the input guardrails.
- Agent 2 (reasoner): overall_status is consistent with the verdicts it
  was given (e.g. don't allow "PASS" if any requirement is FAIL/UNKNOWN);
  gaps/risks aren't empty when there ARE FAIL/UNKNOWN verdicts.
- General: no leaked instructions/system-prompt text in the output, no
  fields that look like they echoed raw attacker-controlled text verbatim
  into a "recommended_action" in a way that could be a second-order
  injection if this report is ever fed to another system.

Hints:
- @output_guardrail functions receive the agent's final output
  (already validated against output_type by Pydantic) -- this is for
  *semantic* checks Pydantic types can't express, not shape validation.
- Return GuardrailFunctionOutput(tripwire_triggered=True, ...) to block
  a bad result from going out; main.py should treat that as "retry or
  surface a clear internal error," not silently pass through.
"""

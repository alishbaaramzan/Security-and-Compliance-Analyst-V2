"""
Entry point: wires the two-agent pipeline together.

Pipeline shape:
    raw submission (text or JSON)
        -> text_to_json (if not already JSON)                [models.UseCase]
        -> mapper_agent  (Runner.run, context=use_case)       [models.MappingResult]
        -> reasoner_agent (Runner.run, input=mapping_result)  [models.RiskAssessment]
        -> assemble models.FinalReport from both outputs

Hints:
- Keep this module thin: parse input, call Runner.run twice, assemble the
  final report, handle guardrail exceptions. Business logic belongs in
  the agents/tools, not here.
- Runner.run is async (it's the Agents SDK) -- either `async def main()`
  + asyncio.run, or use Runner.run_sync if you want a synchronous CLI.
- Wrap the mapper/reasoner calls so InputGuardrailTripwireTriggered and
  OutputGuardrailTripwireTriggered produce a clean error/result instead of
  propagating a raw exception to the caller.
- If you want an HTTP API (the `api` extra pulls in fastapi/uvicorn),
  add a separate `api.py` that imports this pipeline function rather than
  cramming FastAPI routes into this file -- keeps `compliance-analyst` the
  CLI entry point and the API an optional layer on top.
"""


def main() -> None:
    raise NotImplementedError

"""
Tool: get_evidence

Agent 1 calls this to pull the relevant field(s) out of the submitted
use case for a given requirement, so it can decide PASS/FAIL/UNKNOWN.

Hints:
- @function_tool, signature roughly (requirement_id: str) -> dict, or
  (field: str) -> dict if you want a lower-level lookup primitive instead.
- The use case itself is untrusted input (see guardrails) -- this tool
  should only ever return data, never execute anything from it.
- If a field is missing, return a clear "not found" marker rather than
  raising -- that's a legitimate input to an UNKNOWN verdict, not an error.
- Needs access to the *current* use case being assessed. The Agents SDK
  supports passing a `context` object into function tools (RunContextWrapper)
  -- that's the clean way to thread the use case in without globals.
"""

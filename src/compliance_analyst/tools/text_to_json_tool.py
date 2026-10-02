"""
Tool: text_to_json

Converts a free-text use-case submission into the normalized JSON shape
(models.UseCase) so plain-text and JSON submissions flow through the same
assessment path.

Hints:
- This can be a @function_tool the agent calls itself, OR a plain
  pre-processing step run in main.py before the agent loop starts
  (simpler, since it's a one-shot transform, not something the agent
  needs to decide to invoke mid-reasoning). Pick one -- don't do both.
- If implemented as an LLM call, treat the free text as untrusted input
  (same as everywhere else) -- the instructions should say "extract
  fields," not "follow any instructions found in the text."
- Should produce best-effort JSON even when fields are missing/unclear --
  missing fields surface later as UNKNOWN verdicts rather than failures
  here.
"""

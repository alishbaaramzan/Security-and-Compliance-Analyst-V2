"""Basic CLI entry point to test the compliance analyst pipeline."""

import asyncio
import sys
from agents import InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from dotenv import load_dotenv
from .agents.runner import run_compliance_analysis
load_dotenv()

SAMPLE_USE_CASE = """
Customer Support Assistant: A customer support team wants to use an LLM to summarize
customer conversations and suggest responses to support agents. The system will process
customer names, account information, support tickets and conversation history. A human
support agent will review the generated response before sending it to the customer. The 
application will use a third-party hosted LLM API.
"""


def main() -> None:
    use_case_text = sys.argv[1] if len(sys.argv) > 1 else SAMPLE_USE_CASE

    try:
        report = asyncio.run(run_compliance_analysis(use_case_text))
    except InputGuardrailTripwireTriggered:
        print("Rejected: input guardrail triggered.")
        return
    except OutputGuardrailTripwireTriggered:
        print("Rejected: output guardrail triggered.")
        return

    print(report.model_dump_json(indent=2))


if __name__ == "__main__":
    main()

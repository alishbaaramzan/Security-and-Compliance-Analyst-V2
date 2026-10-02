"""
Agent 1: Compliance Mapper
"""

from agents import Agent
from ..guardrails.input_guardrails import check_use_case_input
from ..guardrails.output_guardrails import check_mapping_completeness
from ..models import MappingResult
from ..tools.evidence_tool import get_required_evidence
from ..tools.requirements_tool import get_requirements
from ..tools.text_to_json_tool import convert_text_to_json

compliance_mapper_agent = Agent(
    name="Compliance Mapper",
    instructions=(
        "You are a compliance analyst agent. Convert the submitted use "
        "case to JSON, get the requirements and the evidence needed for "
        "each, and return a verdict (PASS, FAIL, or UNKNOWN) with "
        "evidence for every requirement."
    ),
    tools=[
        get_requirements,
        get_required_evidence,
        convert_text_to_json,
    ],
    output_type=MappingResult,
    input_guardrails=[check_use_case_input],
    output_guardrails=[check_mapping_completeness],
)

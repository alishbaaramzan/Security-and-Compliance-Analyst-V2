"""
Agent 1: Compliance Mapper
"""

from agents import Agent
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
)

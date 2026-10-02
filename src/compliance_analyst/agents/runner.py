"""Calling the agents to run the compliance analysis."""

from agents import Runner
from .mapper_agent import compliance_mapper_agent
from .reasoner_agent import reasoner_agent
from ..models import FinalReport


async def run_compliance_analysis(use_case_text: str) -> FinalReport:
    mapper_result = await Runner.run(compliance_mapper_agent, use_case_text)
    mapping_result = mapper_result.final_output

    reasoner_result = await Runner.run(
        reasoner_agent, mapping_result.model_dump_json()
    )
    risk_assessment = reasoner_result.final_output

    return FinalReport(
        requirement_verdicts=mapping_result.requirement_verdicts,
        overall_status=risk_assessment.overall_status,
        gaps=risk_assessment.gaps,
        risks=risk_assessment.risks,
        next_steps=risk_assessment.next_steps,
    )
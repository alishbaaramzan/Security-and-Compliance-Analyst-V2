"""
Agent 2: Risk Reasoner
"""
from agents import Agent
from ..models import RiskAssessment

reasoner_agent = Agent(
    name="Risk Reasoner",
    instructions=(
        "You are a compliance analyst agent. You will receive a list of "
        "requirements and their compliance status. Analyze the information "
        "and provide a comprehensive risk assessment."
    ),
    output_type=RiskAssessment,
)

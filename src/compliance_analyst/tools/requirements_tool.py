"""
Tool to return the requirements data for the compliance analyst agent 1
"""

import json
from .requirements_data import REQUIREMENTS
from agents.decorators import function_tool

@function_tool
async def get_requirements() -> list[dict]:
    """Return all security requirements.    
    """
    return REQUIREMENTS
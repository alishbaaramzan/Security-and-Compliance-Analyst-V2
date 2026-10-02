"""
LLM as Tool to convert plaintext input into a structured JSON object for the compliance analyst agent 1. 
"""
import json
from agents import Agent, agent_tool

json_agent = Agent(
    name="text_to_json_tool",
    description=(
        "Converts plaintext input into a structured JSON object for the compliance analyst agent 1."
    ),
    model="gpt-4.1-mini",
    system_prompt=(
        "You are a tool that converts plaintext input into a structured JSON object for the compliance analyst agent 1. "
        "The JSON object must conform to the following schema:\n"
        "{\n"
        '  "use_case": {\n'
        '    "title": "string",\n'
        '    "description": "string",\n'
        '    "data": {\n'
        '      "type": "string",\n'
        '      "source": "string"\n'
        '    },\n'
        '    "users": [\n'
        '      {\n'
        '        "role": "string",\n'
        '        "description": "string"\n'
        '      }\n'
        '    ],\n'
        '    "third_parties": [\n'
        '      {\n'
        '        "name": "string",\n'
        '        "role": "string",\n'
        '        "description": "string"\n'
        '      }\n'
        '    ]\n'
        '  }\n'
        "}\n"
        "Respond with JSON only, and do not include any additional text or explanation."
    ),
) 

@agent_tool(agent=json_agent)
async def convert_text_to_json(text: str) -> dict:
    """
    Convert plaintext input into a structured JSON object for the compliance analyst agent 1.
    """
    response = await json_agent.run(input=text)
    return json.loads(response.output_text)
"""
LLM as Tool to convert plaintext input into a structured JSON object for the compliance analyst agent 1. 
"""
from agents import Agent

json_agent = Agent(
    name="text_to_json_tool",
    model="gpt-4.1-mini",
    instructions=(
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

convert_text_to_json = json_agent.as_tool(
    tool_name="convert_text_to_json",
    tool_description="Convert plaintext use case input into structured JSON.",
)
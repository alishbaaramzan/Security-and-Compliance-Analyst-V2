# Compliance Analyst

It is an AI powered assessment of AI use cases against requirements AI-001..AI-008.
It is built with the OpenAI Agents Python SDK.

## Architecture
```
use case (text/JSON)
   -> Compliance Mapper (Agent 1)
        tools: convert_text_to_json, get_requirements, get_required_evidence
        output: MappingResult (verdict + evidence + action, per requirement)
   -> Risk Reasoner (Agent 2)
        no tools, reasons over Agent 1's output only
        output: RiskAssessment (overall_status, gaps, risks, next_steps)
   -> FinalReport
   ```

agents/runner.py::run_compliance_analysis() runs both agents in sequence and assembles final report`.

Here orchestration is done both as code and tool in two different scanrios:

- The convert_text_to_json tool is essentially an agent as tool. The reason why this agent was used as tool is because it's work is triggered just once, gets finished and then the control goes to the mapping agent.
- The two main agents (mapping agent and reasoning agent) are orchestrated as code for more control and visibility, and also because they simply had to be called in sequence.

## Guardrails

- Input: rejects empty submissions -> InputGuardrailTripwireTriggered.
- Output: every requirement ID must have a verdict -> OutputGuardrailTripwireTriggered.

## Output Screenshots

<img width="952" height="471" alt="Screenshot 2026-10-02 194339" src="https://github.com/user-attachments/assets/971c0b58-36a8-478a-a75a-8bb5c7bd4a49" />

<img width="308" height="344" alt="Screenshot 2026-10-02 194417" src="https://github.com/user-attachments/assets/d3acbf33-d35c-40b3-83fc-a7331db6d816" />

<img width="329" height="244" alt="Screenshot 2026-10-02 194424" src="https://github.com/user-attachments/assets/6afe8a86-7df2-4bb9-b9e0-177c372c659a" />



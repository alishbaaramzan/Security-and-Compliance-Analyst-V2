"""Minimal FastAPI app serving the frontend and the /assess endpoint."""

from pathlib import Path

from agents import InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .agents.runner import run_compliance_analysis

load_dotenv()

app = FastAPI(title="Compliance Analyst")

WEB_DIR = Path(__file__).parent / "web"


class AssessRequest(BaseModel):
    use_case: str


@app.get("/")
def index():
    return FileResponse(WEB_DIR / "index.html")


@app.post("/assess")
async def assess(request: AssessRequest):
    try:
        report = await run_compliance_analysis(request.use_case)
    except InputGuardrailTripwireTriggered:
        raise HTTPException(status_code=400, detail="Input guardrail triggered.")
    except OutputGuardrailTripwireTriggered:
        raise HTTPException(status_code=500, detail="Output guardrail triggered.")

    return report.model_dump()


app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

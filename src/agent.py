from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

# Sub-agents
from app.agents.threat_intake import extract_iocs, intake_agent
from app.agents.analyzer import score_threat, analyzer_agent
from app.agents.reporter import generate_markdown_report

import asyncio


SYSTEM_PROMPT = """
You are an AI Cyber Threat Intelligence Agent.
Your job: extract IOCs, analyze threats, score risk, map MITRE ATT&CK,
and generate clear structured threat reports.
"""


# -----------------------------
# Async pipeline
# -----------------------------
async def analyze_pipeline(text: str):
    iocs = extract_iocs(text)

    enriched = await intake_agent.run_async(f"Explain these IOCs:\n{iocs}")

    score = score_threat(iocs)

    summary = await analyzer_agent.run_async(
        f"Summarize this threat:\n{iocs}"
    )

    report_input = {
        "summary": summary,
        "details": iocs,
        "score": score,
    }

    return generate_markdown_report(report_input)


# -----------------------------
# Function-based tool (ADK old API)
# -----------------------------
def threat_pipeline(text: str) -> str:
    """
    Run full CTI processing pipeline:
    IOC extraction → analysis → scoring → markdown report.
    """
    return asyncio.run(analyze_pipeline(text))


# -----------------------------
# Root Agent
# -----------------------------
root_agent = LlmAgent(
    name="ThreatIntelAgent",
    model="gemini-2.0-flash",
    system_prompt=SYSTEM_PROMPT,
    tools=[google_search, threat_pipeline],
)

# app/agent.py
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
import json

# Import our custom tools
from app.tools.cve_lookup import cve_lookup
from app.tools.intel_scraper import scrape_threat_intel
from app.tools.log_parser import parse_security_logs
from app.tools.system_prompt_tool import get_system_prompt

# Sub-agents & functions
from app.agents.threat_intake import extract_iocs
from app.agents.analyzer import score_threat
from app.agents.reporter import generate_markdown_report

# ----------------------------
# Threat pipeline tool
# ----------------------------
async def _threat_pipeline(text: str) -> str:
    """
    Full async threat analysis pipeline.
    Returns stringified JSON for ADK compatibility.
    """
    try:
        # 1. Extract IOCs
        iocs = extract_iocs(text)
        
        # 2. Simple enrichment
        total_iocs = sum(len(v) for v in iocs.values())
        enriched = f"Extracted {total_iocs} IOCs including: "
        ioc_types = []
        for ioc_type, values in iocs.items():
            if values:
                ioc_types.append(f"{len(values)} {ioc_type}")
        enriched += ", ".join(ioc_types)
        
        # 3. Score threat
        score_result = score_threat(iocs)
        
        # 4. Build markdown report
        report = generate_markdown_report({
            "summary": f"Threat analysis completed - Score: {score_result.get('score', 0)}/100",
            "details": iocs,
            "score": score_result,
            "enriched": enriched,
        })

        # 5. Return as JSON string
        return json.dumps({
            "content": report,
            "score": score_result.get("score", 0),
            "error": False
        })
    except Exception as e:
        return json.dumps({
            "content": f"Error in threat pipeline: {str(e)}",
            "score": 0,
            "error": True
        })

# Create FunctionTool instances
threat_tool = FunctionTool(_threat_pipeline)
cve_tool = FunctionTool(cve_lookup)
intel_tool = FunctionTool(scrape_threat_intel)
log_tool = FunctionTool(parse_security_logs)
prompt_tool = FunctionTool(get_system_prompt)

# Main Agent Configuration
root_agent = LlmAgent(
    name="ThreatIntelAgent",
    model="gemini-2.0-flash",
    tools=[threat_tool, cve_tool, intel_tool, log_tool, prompt_tool]
)
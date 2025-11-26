# app/agent.py
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
import json

# Import custom tools 
from app.tools.cve_lookup import cve_lookup
from app.tools.intel_scraper import scrape_threat_intel
from app.tools.log_parser import parse_security_logs
from app.tools.system_prompt_tool import get_system_prompt
from app.memory.longterm_memory import store_threat_intel
from app.memory.session_store import store_session
from app.evaluation.threat_scoring import evaluate_threat_score
from app.observability.logs import setup_logging
from app.observability.tracing import tracer, get_agent_traces
from app.middleware.system_prompt import get_enhanced_system_prompt
from app.agents.reporter import generate_clean_report

# Sub-agents & functions
from app.agents.threat_intake import extract_iocs
from app.agents.analyzer import score_threat
from app.agents.reporter import generate_markdown_report

# ----------------------------
# Threat pipeline tool
# ----------------------------
async def _threat_pipeline(text: str) -> str:
    try:
        iocs = extract_iocs(text)
        
        total_iocs = sum(len(v) for v in iocs.values())
        enriched = f"Extracted {total_iocs} IOCs including: "
        ioc_types = []
        for ioc_type, values in iocs.items():
            if values:
                ioc_types.append(f"{len(values)} {ioc_type}")
        enriched += ", ".join(ioc_types)
        
        score_result = score_threat(iocs)
        
        report = generate_markdown_report({
            "summary": f"Threat analysis completed - Score: {score_result.get('score', 0)}/100",
            "details": iocs,
            "score": score_result,
            "enriched": enriched,
        })

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

# Create FunctionTool instances for all tools
threat_tool = FunctionTool(_threat_pipeline)
cve_tool = FunctionTool(cve_lookup)
intel_tool = FunctionTool(scrape_threat_intel)
log_tool = FunctionTool(parse_security_logs)
prompt_tool = FunctionTool(get_system_prompt)
store_intel_tool = FunctionTool(store_threat_intel)
store_session_tool = FunctionTool(store_session)
score_tool = FunctionTool(evaluate_threat_score)
logging_tool = FunctionTool(setup_logging)
enhanced_prompt_tool = FunctionTool(get_enhanced_system_prompt)
clean_report_tool = FunctionTool(generate_clean_report)
tracing_tool = FunctionTool(get_agent_traces)

# Main Agent Configuration with all tools
root_agent = LlmAgent(
    name="ThreatIntelAgent",
    model="gemini-2.0-flash",
    tools=[
        threat_tool,           # Original threat pipeline
        cve_tool,              # CVE lookup
        intel_tool,            # Threat intelligence scraping
        log_tool,              # Security log parsing
        prompt_tool,           # System prompt getter
        store_intel_tool,      # Threat intelligence storage
        store_session_tool,    # Session context storage
        score_tool,            # Threat scoring
        logging_tool,          # Logging configuration
        enhanced_prompt_tool,  # Enhanced capabilities
        clean_report_tool,      # Clean report generation
        tracing_tool           # Observability and tracing 
    ]
)

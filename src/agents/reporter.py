"""
Reporter sub-agent + helpers.

- Turn analyzed results into Markdown, JSON, or brief summaries.
- Exposes reporter_agent (LlmAgent) for LLM-driven report refinement.
"""

from typing import Dict, Any
from google.adk.agents.llm_agent import LlmAgent
import json
import datetime

def generate_markdown_report(analysis: Dict[str, Any]) -> str:
    """
    Create a readable markdown report from analysis dict.
    """
    now = datetime.datetime.utcnow().isoformat() + "Z"
    md = [
        f"# Threat Report",
        f"_Generated: {now}_",
        "",
    ]
    summary = analysis.get("summary") or analysis.get("threat_summary") or "No summary available."
    md.append("## Summary")
    md.append(summary)
    md.append("")

    score = analysis.get("score") or analysis.get("threat_score") or analysis.get("score", {})
    md.append("## Score")
    md.append(str(score))
    md.append("")

    md.append("## Details")
    details = analysis.get("details") or {}
    md.append("```json")
    md.append(json.dumps(details, indent=2))
    md.append("```")
    md.append("")
    return "\n".join(md)

def generate_json_report(analysis: Dict[str, Any]) -> str:
    """
    Return a compact JSON report string.
    """
    return json.dumps(analysis, indent=2)

reporter_agent = LlmAgent(
    name="ThreatReporterAgent",
    model="gemini-2.0-flash",
   # reporter usually does not need external tools
)

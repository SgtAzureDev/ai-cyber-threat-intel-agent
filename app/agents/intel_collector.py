"""
Intel collector sub-agent + helper utilities.
"""

from typing import Dict, Any, List
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search


def enrich_iocs_stub(iocs: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Lightweight local enrichment stub.
    """
    enriched = {}
    for k, values in iocs.items():
        enriched[k] = []
        for v in values:
            enriched[k].append({
                "value": v,
                "enrichment": {
                    "notes": "no-data-stub",
                    "confidence": 0.0,
                }
            })
    return enriched


# ---- REQUIRED BY AGENT LOADER ----
def enrich_iocs(iocs: Dict[str, List[str]]) -> Dict[str, Any]:
    """Compatibility wrapper used by main ThreatIntelAgent."""
    return enrich_iocs_stub(iocs)


collector_agent = LlmAgent(
    name="IntelCollectorAgent",
    model="gemini-2.0-flash",
    tools=[google_search],
)

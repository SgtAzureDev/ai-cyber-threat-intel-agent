"""
Intel collector sub-agent + helper utilities.

- Enriches IOCs using available tools (google_search) or lightweight stubs.
- Exposes collector_agent (LlmAgent) to perform higher-level enrichment using LLM + tools.
"""

from typing import Dict, Any, List
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

def enrich_iocs_stub(iocs: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Lightweight local enrichment stub. Returns a structure with each IOC and a placeholder
    'enrichment' field. Replace or extend with real tool integrations (VT, Shodan, NVD).
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

collector_agent = LlmAgent(
    name="IntelCollectorAgent",
    model="gemini-2.0-flash",
    tools=[google_search],
)

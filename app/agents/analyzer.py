"""
Analyzer sub-agent + helpers.

- Provides a simple scoring function and MITRE mapping stub.
- Exposes analyzer_agent (LlmAgent) for LLM-powered analysis and TTP mapping.
"""

from typing import Dict, Any
from google.adk.agents.llm_agent import LlmAgent

def score_threat(enriched_iocs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Very simple heuristic scorer.
    Assigns points per IOC type and returns an overall risk score 0-100.
    """
    score = 0
    weights = {
        "ips": 10,
        "urls": 15,
        "domains": 8,
        "sha256": 25,
        "sha1": 20,
        "md5": 10,
    }
    for k, items in enriched_iocs.items():
        count = len(items or [])
        score += weights.get(k, 5) * count

    # clamp to 100
    final = max(0, min(100, score))
    return {"score": final, "details": {"raw_score": score}}

def map_to_mitre(summary_text: str) -> Dict[str, Any]:
    """
    MITRE ATT&CK mapping stub. Returns a minimal mapping structure.
    Replace with a more sophisticated mapping (embedding similarity or LLM prompt) later.
    """
    # naive placeholder
    return {"techniques": [], "tactics": []}

analyzer_agent = LlmAgent(
    name="ThreatAnalyzerAgent",
    model="gemini-2.0-flash",
# no tools by default — analyzer works on collected/enriched data
)

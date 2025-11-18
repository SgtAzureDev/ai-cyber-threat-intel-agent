from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

root_agent = LlmAgent(
    name="ThreatIntelAgent",
    model="gemini-2.0-flash",
    system_prompt=(
        "You are a cyber threat intelligence analysis agent. "
        "Analyze logs, threat reports, indicators of compromise, "
        "detect malicious patterns, summarize threats, "
        "and provide structured intelligence insights."
    ),
    tools=[google_search],
)

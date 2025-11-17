from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools import google_search

agent = LlmAgent(
    name="ThreatIntelAgent",
    model="gemini-2.0-flash",
    prompt_template="Analyze cyber threat intelligence data and generate insights.",
    tools=[google_search],
)

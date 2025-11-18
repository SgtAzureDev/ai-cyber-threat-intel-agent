from google.adk.agents.llm_agent import LlmAgent

class SystemPromptInjector:
    """
    Middleware wrapper. Does NOT subclass LlmAgent.
    """

    def __init__(self, agent: LlmAgent, system_prompt: str):
        self.agent = agent          # store wrapped agent
        self.system_prompt = system_prompt

    def _inject(self, message: str) -> str:
        return (
            f"SYSTEM: {self.system_prompt}\n\n"
            f"USER: {message}"
        )

    def run(self, user_message: str):
        wrapped = self._inject(user_message)
        return self.agent.run(wrapped)

    async def run_sse(self, user_message: str, send_event):
        wrapped = self._inject(user_message)
        return await self.agent.run_sse(wrapped, send_event)

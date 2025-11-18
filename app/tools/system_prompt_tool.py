from google.adk.tools import BaseTool

class SystemPromptTool(BaseTool):
    name = "inject_system_prompt"
    description = "Adds system prompt before user message."

    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def run(self, message: str) -> str:
        return (
            f"SYSTEM: {self.system_prompt}\n\n"
            f"USER: {message}"
        )

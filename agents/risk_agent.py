class RiskAgent:
    SYSTEM_PROMPT = "You are a risk and compliance expert. Identify security, operational, and regulatory risks."

    def run(self, llm, context: str) -> str:
        return llm.generate(self.SYSTEM_PROMPT, context)

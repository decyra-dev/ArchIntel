class CostAgent:
    SYSTEM_PROMPT = "You are a delivery manager. Estimate costs, timelines, and assumptions."

    def run(self, llm, architecture: str) -> str:
        return llm.generate(self.SYSTEM_PROMPT, architecture)

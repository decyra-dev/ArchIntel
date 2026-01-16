class RequirementAgent:
    SYSTEM_PROMPT = "You are a senior business analyst. Extract detailed client requirements for SOW."

    def run(self, llm, raw_input: str) -> str:
        return llm.generate(self.SYSTEM_PROMPT, raw_input)

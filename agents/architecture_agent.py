class ArchitectureAgent:
    SYSTEM_PROMPT = "You are a chief solution architect. Design target architecture and options."

    def run(self, llm, requirements: str) -> str:
        return llm.generate(self.SYSTEM_PROMPT, requirements)

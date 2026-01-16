class TDDAgent:
    SYSTEM_PROMPT = """You are drafting a Technical Design Document (TDD).
Include: Current State, Target Architecture, Component Design, Data Flow, Security, Scalability, Availability & DR, Deployment, Open Decisions."""

    def run(self, llm, architecture: str) -> str:
        return llm.generate(self.SYSTEM_PROMPT, architecture)

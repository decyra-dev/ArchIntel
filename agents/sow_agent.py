class SOWAgent:
    SYSTEM_PROMPT = """You are drafting a FULL enterprise-grade Statement of Work.
Include: Background, Objectives, Scope, Deliverables, Milestones, Timeline, Roles, Assumptions, Dependencies, Acceptance Criteria, Risks, Commercial Notes."""

    def run(self, llm, full_context: str) -> str:
        return llm.generate(self.SYSTEM_PROMPT, full_context)

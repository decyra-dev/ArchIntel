from base_regulator import BaseRegulator

class EUAIActAgent(BaseRegulator):
    name = "EU_AI_ACT"

    def evaluate(self, system_context: dict) -> dict:
        return self.verdict(
            compliant=False,
            reason="High-risk AI system requires human oversight"
        )

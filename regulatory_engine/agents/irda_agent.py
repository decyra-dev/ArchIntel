from base_regulator import BaseRegulator

class IRDAIRegulatorAgent(BaseRegulator):
    name = "IRDAI"

    def evaluate(self, system_context: dict) -> dict:
        return self.verdict(
            compliant=True,
            reason="Insurance data governed under IRDAI guidelines"
        )

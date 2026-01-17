from base_regulator import BaseRegulator

class ISO27001Agent(BaseRegulator):
    name = "ISO27001"

    def evaluate(self, system_context: dict) -> dict:
        return self.verdict(
            compliant=True,
            reason="Information Security Management System in place"
        )

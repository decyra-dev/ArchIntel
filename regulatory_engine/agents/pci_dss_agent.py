from base_regulator import BaseRegulator

class PCIDSSAgent(BaseRegulator):
    name = "PCI_DSS"

    def evaluate(self, system_context: dict) -> dict:
        return self.verdict(
            compliant=False,
            reason="Payment data encryption not enforced at rest"
        )

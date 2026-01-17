from regulatory_engine.base_regulator import BaseRegulator


class RBIRegulatorAgent(BaseRegulator):
    name = "RBI"

    def evaluate(self, context: dict) -> dict:
        return {
            "regulator": self.name,
            "status": "REQUIRED",
            "focus_areas": [
                "Data localization",
                "IT governance",
                "Outsourcing risk",
                "Audit trails",
                "BCP & DR"
            ],
            "notes": "Applies to Indian banking and financial institutions."
        }

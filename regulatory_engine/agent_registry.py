from abc import ABC, abstractmethod

# --------------------------------------------------
# BASE CLASS
# --------------------------------------------------
class BaseRegulator(ABC):
    @abstractmethod
    def evaluate(self, context: dict):
        """Must return a dict with 'regulator' and 'requirement' keys."""
        pass

# --------------------------------------------------
# INDIVIDUAL AGENT CLASSES
# --------------------------------------------------

class RBIRegulatorAgent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "RBI (Reserve Bank of India)",
            "requirement": "Mandatory data localization. All payment data must be stored exclusively in India."
        }

class IRDAIRegulatorAgent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "IRDAI (Insurance Regulatory and Development Authority)",
            "requirement": "Compliance with Insurance Information Bureau (IIB) data standards and cybersecurity guidelines."
        }

class HIPAARegulatorAgent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "HIPAA (US Healthcare)",
            "requirement": "Encryption of PHI (Protected Health Information) and execution of Business Associate Agreements."
        }

class GDPRAgent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "GDPR (EU Privacy)",
            "requirement": "Implementation of Data Protection Impact Assessments (DPIA) and Right to Erasure protocols."
        }

class EUAIAgent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "EU AI Act",
            "requirement": "Risk-based classification of AI systems. High-risk systems require strict data governance and human oversight."
        }

class PCIDSSAgent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "PCI DSS (Payment Card Industry)",
            "requirement": "Strict firewall configuration, encryption of cardholder data, and regular security testing."
        }

class SOC2Agent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "SOC 2 (Type II)",
            "requirement": "Audit-ready evidence for Trust Services Criteria: Security, Availability, and Confidentiality."
        }

class ISO27001Agent(BaseRegulator):
    def evaluate(self, context: dict):
        return {
            "regulator": "ISO/IEC 27001",
            "requirement": "Establishment of an Information Security Management System (ISMS) with continuous risk treatment."
        }

# --------------------------------------------------
# THE REGISTRY (Mapping Matrix strings to Class Instances)
# --------------------------------------------------
# This is what app.py uses to find the right agent.
AGENT_REGISTRY = {
    "RBI": RBIRegulatorAgent(),
    "IRDAI": IRDAIRegulatorAgent(),
    "HIPAA": HIPAARegulatorAgent(),
    "GDPR": GDPRAgent(),
    "EU_AI_ACT": EUAIAgent(),
    "PCI_DSS": PCIDSSAgent(),
    "SOC2": SOC2Agent(),
    "ISO27001": ISO27001Agent()
}
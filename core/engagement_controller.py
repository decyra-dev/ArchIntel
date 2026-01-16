from llm.azure_client import AzureLLMClient
from agents.requirement_agent import RequirementAgent
from agents.architecture_agent import ArchitectureAgent
from agents.cost_agent import CostAgent
from agents.risk_agent import RiskAgent
from agents.sow_agent import SOWAgent
from agents.tdd_agent import TDDAgent

class EngagementController:
    def __init__(self, state):
        self.state = state
        self.llm = AzureLLMClient()

    def run(self):
        self.state.requirements = RequirementAgent().run(self.llm, self.state.raw_input)
        self.state.architecture = ArchitectureAgent().run(self.llm, self.state.requirements)
        self.state.costs = CostAgent().run(self.llm, self.state.architecture)
        self.state.risks = RiskAgent().run(
            self.llm,
            self.state.requirements + "\n" + self.state.architecture
        )

    def generate_sow(self):
        context = (
            f"Requirements:\n{self.state.requirements}\n\n"
            f"Architecture:\n{self.state.architecture}\n\n"
            f"Costs:\n{self.state.costs}\n\n"
            f"Risks:\n{self.state.risks}"
        )
        self.state.sow = SOWAgent().run(self.llm, context)

    def generate_tdd(self):
        self.state.tdd = TDDAgent().run(self.llm, self.state.architecture)

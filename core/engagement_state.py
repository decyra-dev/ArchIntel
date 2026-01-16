from dataclasses import dataclass

@dataclass
class EngagementState:
    raw_input: str = ""
    requirements: str = ""
    architecture: str = ""
    costs: str = ""
    risks: str = ""
    sow: str = ""
    tdd: str = ""

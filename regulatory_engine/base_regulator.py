from abc import ABC, abstractmethod
from typing import Dict


class BaseRegulator(ABC):
    """
    Base class for all regulatory agents.
    """

    name: str = "BASE"

    @abstractmethod
    def evaluate(self, context: Dict) -> Dict:
        """
        Evaluate compliance based on provided context.
        Must be implemented by every regulator agent.
        """
        pass

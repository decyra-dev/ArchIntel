from typing import List, Dict

class RegulatorySelector:
    """
    Decides which regulatory agents must be invoked based on nested 
    conditions in the REGULATORY_MATRIX.
    """

    def __init__(self, country: str, industry: str, data_types: List[str]):
        # Normalize inputs to lowercase for consistent matching
        self.country = str(country).strip().lower()
        self.industry = str(industry).strip().lower()
        # multiselect returns a list; we ensure all items are lowercased
        self.data_types = [str(d).strip().lower() for d in data_types]

    def _matches_rule(self, rule: Dict) -> bool:
        """
        Checks if the user's context satisfies the nested 'conditions' in a rule.
        """
        conditions = rule.get("conditions", {})
        
        # 1. Geography Check (if rule specifies country)
        if "country" in conditions:
            if self.country != conditions["country"].lower():
                return False
        
        # 2. Industry Check (if rule specifies industry)
        if "industry" in conditions:
            if self.industry != conditions["industry"].lower():
                return False
                
        # 3. Data Types Check (if rule specifies data_types)
        if "data_types" in conditions:
            rule_data = [d.lower() for d in conditions["data_types"]]
            # Match if at least one selected data type is in the rule's list
            if not any(dt in rule_data for dt in self.data_types):
                return False

        # 4. System Type Check (specific to AI rules)
        if "system_type" in conditions:
            if "ai" != conditions["system_type"].lower():
                return False

        return True

    def select_agents(self, context: Dict = None) -> List[str]:
        """
        Iterates through the matrix and returns a list of unique agent keys.
        """
        # Local import to avoid circular dependency issues
        from regulatory_engine.regulatory_map import REGULATORY_MATRIX
        
        matched_agents = set()
        for rule in REGULATORY_MATRIX:
            if self._matches_rule(rule):
                for agent_key in rule.get("agents", []):
                    matched_agents.add(agent_key)
        
        return list(matched_agents)
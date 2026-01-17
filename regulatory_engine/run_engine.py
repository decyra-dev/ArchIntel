from regulatory_selector import RegulatorySelector
from agent_registry import AGENT_REGISTRY

SYSTEM_CONTEXT = {
    "country": "India",
    "industry": "banking",
    "data_types": ["PII", "Financial", "Payment"],
    "system_type": "AI"
}

selector = RegulatorySelector()
selected_agents = selector.select_agents(SYSTEM_CONTEXT)

print("Applied Regulations:", selected_agents)
print("-" * 50)

results = []
for agent_key in selected_agents:
    agent = AGENT_REGISTRY[agent_key]
    result = agent.evaluate(SYSTEM_CONTEXT)
    results.append(result)
    print(result)

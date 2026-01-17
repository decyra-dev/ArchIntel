# regulatory_engine/regulatory_map.py

REGULATORY_MATRIX = [
    {
        "conditions": {"country": "India", "industry": "banking"},
        "agents": ["RBI", "ISO27001"]
    },
    {
        "conditions": {"country": "India", "industry": "insurance"},
        "agents": ["IRDAI", "ISO27001"]
    },
    {
        "conditions": {"country": "USA", "data_types": ["PHI"]},
        "agents": ["HIPAA", "SOC2"]
    },
    {
        "conditions": {"country": "EU", "system_type": "AI"},
        "agents": ["GDPR", "EU_AI_ACT", "ISO27001"]
    },
    {
        "conditions": {"data_types": ["Payment"]},
        "agents": ["PCI_DSS"]
    }
]
# sow_engine/tdd_composer.py

class TDDComposer:
    """
    Generates a structured Technical Design Document (TDD) for enterprise projects.
    Uses the same regulatory outputs and project context as SOWComposer.
    """

    def __init__(self, client_name, project_title, context, regulators):
        self.client_name = client_name
        self.project_title = project_title
        self.context = context
        self.regulators = regulators

    def compose(self):
        # Start TDD content
        tdd = f"TECHNICAL DESIGN DOCUMENT (TDD)\n"
        tdd += f"Project: {self.project_title}\n"
        tdd += f"Client: {self.client_name}\n"
        tdd += "-"*60 + "\n\n"

        tdd += "1. Overview / Background:\n"
        tdd += f"{self.context}\n\n"

        tdd += "2. System Architecture & Components:\n"
        tdd += "- High-level architecture diagram: [Diagram Placeholder]\n"
        tdd += "- Modules and services involved\n"
        tdd += "- Data flow and integration points\n\n"

        tdd += "3. Data & Compliance Requirements:\n"
        for r in self.regulators:
            tdd += f"- {r.get('regulator', 'Unknown')} Requirements: {', '.join(r.get('focus_areas', []))}\n"
        tdd += "\n"

        tdd += "4. Security Measures:\n"
        tdd += "- Access control\n- Encryption\n- Logging & Monitoring\n- Backup & Recovery\n\n"

        tdd += "5. Interfaces & Integration:\n"
        tdd += "- APIs, ETL pipelines, messaging systems\n- External system integration points\n\n"

        tdd += "6. Deployment & Environment:\n"
        tdd += "- Dev, QA, Staging, Production environments\n- Cloud/on-prem details\n- CI/CD pipeline overview\n\n"

        tdd += "7. Risks & Mitigations:\n"
        tdd += "- Potential technical risks and mitigation strategies\n\n"

        tdd += "8. Assumptions & Constraints:\n"
        tdd += "- Key assumptions about data, system, and users\n- Constraints regarding tech stack or compliance\n\n"

        tdd += "9. Acceptance Criteria:\n"
        tdd += "- System is deployed as per architecture\n- Regulatory requirements met\n- Functional and performance validation completed\n"

        return tdd

from typing import List, Dict


class SOWComposer:
    """
    Composes a full enterprise-grade Statement of Work (SOW)
    using structured inputs and regulatory agent outputs.
    """

    def __init__(
        self,
        client_name: str,
        project_title: str,
        context: str,
        regulators: List[Dict],
    ):
        self.client_name = client_name
        self.project_title = project_title
        self.context = context
        self.regulators = regulators

    # ---------------- CORE SECTIONS ---------------- #

    def compose(self) -> str:
        sections = [
            self._header(),
            self._engagement_overview(),
            self._objectives(),
            self._scope(),
            self._delivery_phases(),
            self._regulatory_obligations(),
            self._assumptions(),
            self._roles_responsibilities(),
            self._risks(),
            self._acceptance_criteria(),
            self._governance(),
            self._compliance_annexure(),
        ]
        return "\n\n".join(sections)

    def _header(self) -> str:
        return f"""
STATEMENT OF WORK (SOW)
Project: {self.project_title}
Client: {self.client_name}
"""

    def _engagement_overview(self) -> str:
        return f"""
1. ENGAGEMENT OVERVIEW

This Statement of Work ("SOW") defines the scope, deliverables,
and responsibilities for the engagement between the Client and
the Service Provider.

Context of the engagement:
{self.context}
"""

    def _objectives(self) -> str:
        return """
2. OBJECTIVES

The primary objectives of this engagement are:
- Successful delivery of the defined technical solution
- Compliance with applicable regulatory and industry standards
- Risk-managed execution with audit-ready documentation
"""

    def _scope(self) -> str:
        return """
3. SCOPE OF WORK

3.1 IN SCOPE
- Requirements analysis and validation
- Architecture and design documentation
- Implementation and migration activities
- Security and compliance alignment
- Knowledge transfer and handover

3.2 OUT OF SCOPE
- Business process re-engineering
- Post go-live operational support unless explicitly agreed
- Third-party licensing and commercial agreements
"""

    def _delivery_phases(self) -> str:
        return """
4. DELIVERY PHASES & MILESTONES

Phase 1: Discovery & Design
- Requirements finalization
- Architecture design
- Compliance mapping

Phase 2: Build & Migration
- Implementation
- Data migration
- Security controls implementation

Phase 3: Validation & Handover
- Testing
- Compliance validation
- Documentation and handover
"""

    # ---------------- REGULATORY INTELLIGENCE ---------------- #

    def _regulatory_obligations(self) -> str:
        section = """
5. REGULATORY & COMPLIANCE OBLIGATIONS
"""

        for r in self.regulators:
            controls = "\n".join([f"- {c}" for c in r.get("focus_areas", [])])

            section += f"""
{r["regulator"]} COMPLIANCE REQUIREMENTS:
The Service Provider shall ensure compliance with {r["regulator"]}
by implementing the following controls:
{controls}

Failure to adhere to these requirements may result in
regulatory non-compliance and associated penalties.
"""

        return section

    def _assumptions(self) -> str:
        return """
6. ASSUMPTIONS & DEPENDENCIES

- Client will provide timely access to systems and stakeholders
- Regulatory interpretations are based on current published guidance
- Any changes in scope or regulation may require SOW revision
"""

    def _roles_responsibilities(self) -> str:
        return """
7. ROLES & RESPONSIBILITIES

Client Responsibilities:
- Provide business requirements and approvals
- Ensure data access and regulatory clarifications

Service Provider Responsibilities:
- Deliver agreed scope
- Maintain compliance alignment
- Provide documentation and reporting
"""

    def _risks(self) -> str:
        return """
8. RISKS & MITIGATION

Key risks include:
- Regulatory changes
- Data quality issues
- Dependency delays

Mitigation strategies include phased delivery,
early compliance validation, and stakeholder reviews.
"""

    def _acceptance_criteria(self) -> str:
        return """
9. ACCEPTANCE CRITERIA

Deliverables shall be deemed accepted when:
- All agreed documents are delivered
- Compliance requirements are addressed
- Client provides written sign-off
"""

    def _governance(self) -> str:
        return """
10. GOVERNANCE & REPORTING

- Weekly status reporting
- Steering committee reviews
- Issue and risk tracking
"""

    def _compliance_annexure(self) -> str:
        annexure = """
11. COMPLIANCE ANNEXURE
"""

        for r in self.regulators:
            annexure += f"""
{r["regulator"]}:
Applicable. Compliance controls addressed across design,
implementation, testing, and documentation phases.
"""

        return annexure

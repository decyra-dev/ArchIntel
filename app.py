import streamlit as st
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import os

from regulatory_engine.regulatory_selector import RegulatorySelector
from regulatory_engine.agent_registry import AGENT_REGISTRY
from sow_engine.sow_composer import SOWComposer
from sow_engine.tdd_composer import TDDComposer

# --------------------------------------------------
# BASE PATHS
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR,"decyra.png")  # Adjust if your image is elsewhere

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="ArchIntel – Agentic Engagement Intelligence",
    layout="wide"
)

st.title("ArchIntel – Agentic Engagement Intelligence")
st.caption("Compliance-aware | Agentic | Enterprise-grade")

# --------------------------------------------------
# CLIENT INPUT
# --------------------------------------------------
st.subheader("Client & Engagement Context")
col1, col2 = st.columns(2)

with col1:
    client_name = st.text_input("Client Name")
    country = st.selectbox("Country", ["India", "USA", "EU"])
    industry = st.selectbox("Industry", ["banking", "healthcare", "technology", "insurance"])

with col2:
    project_title = st.text_input("Project Title")
    data_types = st.multiselect("Data Types Involved", ["PII", "PHI", "Payment", "Logs"])

client_context = st.text_area("Client Problem Statement / Background", height=150)

if "sow_text" not in st.session_state:
    st.session_state.sow_text = None
if "tdd_text" not in st.session_state:
    st.session_state.tdd_text = None

# --------------------------------------------------
# RUN AGENTIC ENGAGEMENT
# --------------------------------------------------
if st.button("Run Agentic Engagement"):

    # Regulatory context for agents
    regulatory_context = {
        "country": country,
        "industry": industry,
        "data_types": data_types,
        "system_type": "AI"
    }

    try:
        # 1️⃣ Select relevant regulatory agents
        selector = RegulatorySelector(
            country=country,
            industry=industry,
            data_types=data_types
        )
        selected_agent_keys = selector.select_agents()

        # 2️⃣ Evaluate each agent
        regulatory_results = []
        for key in selected_agent_keys:
            if key in AGENT_REGISTRY:
                agent = AGENT_REGISTRY[key]
                regulatory_results.append(agent.evaluate(regulatory_context))
            else:
                st.warning(f"Agent '{key}' is defined in matrix but missing in Registry.")

        # 3️⃣ Generate enterprise-grade SOW
        sow_composer = SOWComposer(
            client_name=client_name or "Unknown Client",
            project_title=project_title or "Untitled Project",
            context=client_context or "No context provided",
            regulators=regulatory_results
        )
        st.session_state.sow_text = sow_composer.compose()

        # 4️⃣ Generate Technical Design Document (TDD)
        tdd_composer = TDDComposer(
            client_name=client_name or "Unknown Client",
            project_title=project_title or "Untitled Project",
            context=client_context or "No context provided",
            regulators=regulatory_results
        )
        st.session_state.tdd_text = tdd_composer.compose()

    except Exception as e:
        st.error(f"Engine Error: {e}")

# --------------------------------------------------
# PDF GENERATOR FUNCTION WITH LOGO AND FOOTER
# --------------------------------------------------
def generate_pdf(text, logo_path=LOGO_PATH):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Add logo if exists
    if os.path.exists(logo_path):
        logo = Image(logo_path, width=120, height=50)
        story.append(logo)
        story.append(Spacer(1, 12))
    else:
        print(f"Logo not found at {logo_path}")  # Debug info

    # Add document text
    for line in text.split("\n"):
        story.append(Paragraph(line.replace("&", "&amp;"), styles["Normal"]))

    story.append(Spacer(1, 20))
    story.append(Paragraph("Generated / Developed by Decyra", styles["Normal"]))

    doc.build(story)
    buffer.seek(0)
    return buffer.read()

# --------------------------------------------------
# OUTPUTS – SOW
# --------------------------------------------------
if st.session_state.sow_text:
    st.subheader("Review & Customize Generated SOW")
    st.session_state.sow_text = st.text_area("SOW", value=st.session_state.sow_text, height=400)
    st.download_button(
        "Download SOW as PDF",
        generate_pdf(st.session_state.sow_text),
        "ArchIntel_SOW.pdf"
    )

# --------------------------------------------------
# OUTPUTS – TDD
# --------------------------------------------------
if st.session_state.tdd_text:
    st.subheader("Technical Design Document (TDD)")
    st.session_state.tdd_text = st.text_area("TDD", value=st.session_state.tdd_text, height=400)
    st.download_button(
        "Download TDD as PDF",
        generate_pdf(st.session_state.tdd_text),
        "ArchIntel_TDD.pdf"
    )

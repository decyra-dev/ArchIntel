import streamlit as st
from core.engagement_state import EngagementState
from core.engagement_controller import EngagementController
from io_utils.pdf_generator import generate_pdf

st.set_page_config(page_title="ArchIntel v2", layout="wide")

# Initialize session state
if "state" not in st.session_state:
    st.session_state.state = EngagementState()

state = st.session_state.state
controller = EngagementController(state)

st.title("ArchIntel v2 – Agentic SOW & TDD Generator")

# Client input
state.raw_input = st.text_area(
    "Paste Client Requirement / RFP / Problem Statement",
    height=200,
    value=state.raw_input
)

if st.button("▶ Run Agentic Engagement"):
    if not state.raw_input.strip():
        st.warning("Please enter client input")
    else:
        with st.spinner("Running agents..."):
            controller.run()
        st.success("Analysis complete!")

col1, col2 = st.columns(2)

# SOW Section
with col1:
    if st.button("📄 Generate SOW"):
        controller.generate_sow()

    state.sow = st.text_area("Statement of Work (Editable)", height=400, value=state.sow)

    if st.button("⬇ Download SOW PDF"):
        generate_pdf("outputs/SOW.pdf", state.sow)
        st.success("SOW PDF generated!")

# TDD Section
with col2:
    if st.button("🛠 Generate Technical Design Document"):
        controller.generate_tdd()

    state.tdd = st.text_area("Technical Design Document (Editable)", height=400, value=state.tdd)

    if st.button("⬇ Download TDD PDF"):
        generate_pdf("outputs/TDD.pdf", state.tdd)
        st.success("TDD PDF generated!")

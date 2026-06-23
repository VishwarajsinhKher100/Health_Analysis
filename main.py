import streamlit as st
from app.services import analyze_blood_work

st.set_page_config(page_title="Blood Work Analyzer", layout="wide")

# Initialize session state so data persists between button clicks and page reruns
if "health_summary" not in st.session_state:
    st.session_state.health_summary = ""
if "diet_plan" not in st.session_state:
    st.session_state.diet_plan = ""

st.title("Blood Work Analyzer")

left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("Blood Work Report")
    blood_report = st.text_area(
        label="Paste your report below",
        height=500,
        placeholder="Paste your blood work report here...",
        label_visibility="collapsed"
    )
    analyze_clicked = st.button("Analyze", type="primary", use_container_width=True)

# Trigger logic only runs when the user explicitly clicks the button
if analyze_clicked:
    if not blood_report.strip():
        with left_col:
            st.warning("Please paste a blood work report before analyzing.")
    else:
        with st.spinner("Analyzing your blood work..."):
            summary, diet = analyze_blood_work(blood_report)
            st.session_state.health_summary = summary
            st.session_state.diet_plan = diet

with right_col:
    st.subheader("Health Summary")
    with st.container(border=True, height=240):
        st.markdown(st.session_state.health_summary)

    st.subheader("Suggested Diet Plan")
    with st.container(border=True, height=240):
        st.markdown(st.session_state.diet_plan)
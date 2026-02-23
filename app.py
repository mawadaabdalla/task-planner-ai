import streamlit as st
import pandas as pd
from agent import autonomous_planner

st.set_page_config(page_title="Autonomous AI Planner", layout="wide")

st.title("🤖 Autonomous Task Planner Agent")

goal = st.text_input("Enter your goal")
col1, col2 = st.columns(2)

with col1:
    max_days = st.number_input("Maximum Days", min_value=1, value=30)

with col2:
    max_budget = st.number_input("Maximum Budget", min_value=100, value=10000)

if st.button("Generate Plan") and goal:

    with st.spinner("AI is planning..."):
        plan, evaluation, revision_log = autonomous_planner(goal, max_days, max_budget)

    st.subheader("📋 Task Plan")

    df = pd.DataFrame(plan["tasks"])
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Evaluation")

    st.write(f"Total Days: {evaluation['total_days']} / {max_days}")
    st.progress(min(evaluation["total_days"] / max_days, 1.0))

    st.write(f"Total Cost: {evaluation['total_cost']} / {max_budget}")
    st.progress(min(evaluation["total_cost"] / max_budget, 1.0))

    if evaluation["feasible"]:
        st.success("Plan is feasible ✅")
    else:
        st.error("Plan is not feasible ❌")

    if revision_log:
        st.warning("Revision Attempted")
import streamlit as st
from agent import autonomous_planner

st.title("📝 Autonomous Task Planner Agent")

goal = st.text_input("Enter your goal")
max_days = st.number_input("Maximum Days", min_value=1, value=30)
max_budget = st.number_input("Maximum Budget", min_value=1, value=10000)

if st.button("Generate Plan") and goal:
    plan, evaluation, revision_log = autonomous_planner(goal, max_days, max_budget)
    st.subheader("Plan")
    st.json(plan)
    st.subheader("Evaluation")
    st.write(evaluation)
    st.subheader("Revision Log")
    st.json(revision_log)

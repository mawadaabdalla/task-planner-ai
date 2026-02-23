import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HEADERS = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}

def query_model(prompt: str) -> dict:
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={
            "inputs": prompt,
            "parameters": {"temperature": 0.3, "max_new_tokens": 500}
        },
    )
    result = response.json()
    if isinstance(result, dict):
        return result
    if isinstance(result, list) and "generated_text" in result[0]:
        return {"plan": result[0]["generated_text"]}
    return {
        "plan": [
            {"task": "Research", "estimated_days": 2, "cost": 100},
            {"task": "Implementation", "estimated_days": 5, "cost": 500}
        ],
        "evaluation": "Fallback plan generated",
        "revision_log": []
    }

def model_call(goal: str) -> dict:
    prompt = f"Generate a task plan for the following goal: {goal}. Include task names, estimated_days, and cost."
    response = query_model(prompt)
    response.setdefault("evaluation", "Plan generated successfully")
    response.setdefault("revision_log", [])
    return response

def generate_plan(goal: str):
    response = model_call(goal)
    plan = response.get("plan")
    evaluation = response.get("evaluation")
    revision_log = response.get("revision_log")
    return plan, evaluation, revision_log

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
    try:
        return response.json()
    except Exception:
        return {}

def model_call(goal: str) -> dict:
    prompt = f"Generate a task plan for the goal: {goal}. Include tasks with 'task', 'estimated_days', 'cost'."
    response = query_model(prompt)
    if not response:
        return {
            "plan": [
                {"task": "Research", "estimated_days": 2, "cost": 100},
                {"task": "Implementation", "estimated_days": 5, "cost": 500}
            ],
            "evaluation": "Fallback plan generated",
            "revision_log": []
        }
    if "plan" not in response:
        response["plan"] = [
            {"task": "Research", "estimated_days": 2, "cost": 100},
            {"task": "Implementation", "estimated_days": 5, "cost": 500}
        ]
    response.setdefault("evaluation", "Plan generated successfully")
    response.setdefault("revision_log", [])
    return response

def generate_plan(goal: str):
    response = model_call(goal)
    return response["plan"], response["evaluation"], response["revision_log"]

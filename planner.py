import streamlit as st
import requests
from typing import Tuple, List, Dict

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HEADERS = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}

def query_model(prompt: str) -> Dict:
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={
            "inputs": prompt,
            "parameters": {
                "temperature": 0.3,
                "max_new_tokens": 500
            }
        }
    )
    try:
        return response.json()
    except Exception as e:
        raise ValueError(f"Failed to parse model response: {e}")

def model_call(goal: str) -> Dict:
    response = {
        "plan": [
            {"task": "Research", "duration_days": 2, "cost": 100},
            {"task": "Implementation", "duration_days": 5, "cost": 500}
        ],
        "evaluation": "Initial plan generated successfully",
        "revision_log": []
    }
    return response

def generate_plan(goal: str) -> Tuple[List[Dict], str, List[Dict]]:
    response = model_call(goal)
    if not isinstance(response, dict):
        raise ValueError("Model did not return valid JSON.")
    plan = response.get("plan", [])
    evaluation = response.get("evaluation", "")
    revision_log = response.get("revision_log", [])
    return plan, evaluation, revision_log

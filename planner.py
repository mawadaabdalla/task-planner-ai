import requests
import os
from dotenv import load_dotenv
from utils import extract_json
import json

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}


def query_model(prompt):
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt,
            "parameters": {
                "temperature": 0.3,
                "max_new_tokens": 500,
            }
        },
    )
    return response.json()
def model_call(goal: str) -> dict:
    try:
        response = {
            "plan": [
                {"task": "Research", "duration_days": 2, "cost": 100},
                {"task": "Implementation", "duration_days": 5, "cost": 500}
            ],
            "evaluation": "Initial plan generated successfully",
            "revision_log": []
        }
        return response
    except Exception as e:
        raise ValueError(f"Model did not return valid JSON: {e}")
        
def generate_plan(goal):
    response = model_call(goal)
    try:
        plan = json.loads(response)
    except json.JSONDecodeError:
        print("⚠️ Model returned invalid JSON:")
        print(response)
        plan = {
            "tasks": [],
            "evaluation": "Model returned invalid JSON",
            "revision_log": "Check model response formatting"
        }
    return plan


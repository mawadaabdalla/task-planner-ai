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

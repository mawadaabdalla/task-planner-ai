import requests
import os
from dotenv import load_dotenv
from utils import extract_json

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
    prompt = f"""
You are an expert project planner AI.

Goal: {goal}

Break the goal into logically ordered tasks.

For each task include:
- task_name
- estimated_days (integer)
- estimated_cost (integer)

Return ONLY valid JSON in this format:

{{
  "tasks": [
    {{
      "task_name": "",
      "estimated_days": 0,
      "estimated_cost": 0
    }}
  ]
}}
"""

    output = query_model(prompt)

    if isinstance(output, list):
        text = output[0]["generated_text"]
    else:
        text = str(output)

    plan = extract_json(text)

    if not plan:
        raise ValueError("Model did not return valid JSON.")

    return plan
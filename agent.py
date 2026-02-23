from planner import generate_plan
from evaluator import evaluate_plan

def autonomous_planner(goal: str, max_days: int, max_budget: int):
    plan, evaluation, revision_log = generate_plan(goal)
    evaluation = evaluate_plan(plan, max_days, max_budget)
    return plan, evaluation, revision_log

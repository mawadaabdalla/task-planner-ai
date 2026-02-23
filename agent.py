from planner import generate_plan
from evaluator import evaluate_plan


def autonomous_planner(goal, max_days, max_budget):

    plan = generate_plan(goal)
    evaluation = evaluate_plan(plan, max_days, max_budget)

    revision_log = []

    if not evaluation["feasible"]:
        revised_goal = f"""
Revise the plan for: {goal}

Reduce total days to <= {max_days}
Reduce total cost to <= {max_budget}

Return valid JSON only.
"""
        revision_log.append("Initial plan not feasible. Attempting revision.")

        plan = generate_plan(revised_goal)
        evaluation = evaluate_plan(plan, max_days, max_budget)

    return plan, evaluation, revision_log
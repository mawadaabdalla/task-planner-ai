def evaluate_plan(plan: list, max_days: int, max_budget: int):
    total_days = sum(task.get("estimated_days", 0) for task in plan)
    total_cost = sum(task.get("cost", 0) for task in plan)
    if total_days > max_days and total_cost > max_budget:
        return f"Plan exceeds both max days ({max_days}) and max budget ({max_budget})."
    if total_days > max_days:
        return f"Plan exceeds max days ({max_days})."
    if total_cost > max_budget:
        return f"Plan exceeds max budget ({max_budget})."
    return "Plan is within limits."

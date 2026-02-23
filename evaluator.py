def evaluate_plan(plan: list, max_days: int, max_budget: float):
    total_days = sum(task.get("estimated_days", 0) for task in plan)
    total_cost = sum(task.get("cost", 0) for task in plan)
    if total_days > max_days:
        return f"Plan exceeds max days ({total_days}/{max_days})"
    if total_cost > max_budget:
        return f"Plan exceeds max budget (${total_cost}/{max_budget})"
    return "Plan is within limits"

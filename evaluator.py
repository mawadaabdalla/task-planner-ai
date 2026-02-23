def evaluate_plan(plan, max_days, max_budget):
    total_days = sum(task["estimated_days"] for task in plan["tasks"])
    total_cost = sum(task["estimated_cost"] for task in plan["tasks"])

    feasible = total_days <= max_days and total_cost <= max_budget

    return {
        "total_days": total_days,
        "total_cost": total_cost,
        "feasible": feasible
    }
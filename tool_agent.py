def tool_agent(state):
    milestones = state.milestones
    resources = []
    for milestone in milestones:
        resources.append(f"Search results for: {milestone}")
    return {"resources": resources}
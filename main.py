from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from plan_agent import plan_agent
from tool_agent import tool_agent
from reflection_agent import reflection_agent

class SkillBuilderState(BaseModel):
    input: str
    milestones: list[str] = []
    resources: list[str] = []
    refined_plan: list[str] = []
    status: str = ""

builder = StateGraph(SkillBuilderState)

builder.add_node("Plan", plan_agent)
builder.add_node("Solve", tool_agent)
builder.add_node("Reflect", reflection_agent)

builder.set_entry_point("Plan")
builder.add_edge("Plan", "Solve")
builder.add_edge("Solve", "Reflect")
builder.add_edge("Reflect", END)

graph = builder.compile()

result = graph.invoke({"input": "I want to become a Machine Learning Engineer in 6 months."})
print(result)
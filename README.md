# SkillBuilder AI – Personalized Learning Path Generator (Agentic Workflow with LangGraph)

**SkillBuilder AI** is an intelligent assistant that builds customized learning roadmaps for users based on their career goals. Powered by an agentic workflow using [LangGraph](https://docs.langgraph.dev/), it demonstrates how multiple agents can collaborate to plan, execute, and reflect — simulating human-like reasoning.

This project was built as part of an AI Internship evaluation task and showcases planning, tool use, and reflection agents connected in a dynamic and modular workflow.

##  What It Does

You tell SkillBuilder AI:  
 "I want to become a Machine Learning Engineer in 6 months"

It returns:
- A milestone-based skill plan
- Recommended learning resources for each skill
- A final, refined learning roadmap



## How It Works – Architecture

SkillBuilder AI uses a **LangGraph agentic workflow** with the following agents:

### PlanAgent
- Breaks down the user’s input into structured learning milestones

###  ToolAgent
- Finds useful resources (mocked in this version) for each milestone

###  ReflectionAgent
- Reviews the full plan for completeness and returns the final output

Each agent updates a shared state (`SkillBuilderState`) using `pydantic.BaseModel`, passed through a LangGraph `StateGraph`.


##  Streamlit Interface

Includes a minimal interactive UI built with **Streamlit**:

- Users input their goal
- Click “Generate Learning Path”
- See milestones, resources, and final status on-screen

To run this App
streamlit run app.py

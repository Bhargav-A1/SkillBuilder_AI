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

Project Structure

SkillBuilderAI/
│
├── app.py                               # Streamlit UI
├── main.py                              # LangGraph setup
├── plan_agent.py                        # Milestone generation logic
├── tool_agent.py                        # Resource generator
├── reflection_agent.py                  # Plan evaluator
├── requirements.txt
└── README.md

Installation

Clone the repository:

Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows

Install dependencies:
pip install -r requirements.txt
Run the app:

streamlit run app.py

 Features
- Agentic workflow using LangGraph

- Real-world use case (learning path planning)

- Modular and scalable design

- Interactive frontend (Streamlit)

- Easy to extend with OpenAI, Google Search, or other tools

 Future Enhancements
 Add OpenAI/Claude APIs for real language processing

 Integrate YouTube or GitHub search for live resource recommendations

 Estimate time-to-learn and effort per milestone

 Add memory and feedback loops for iterative planning

Coming Soon: Hosted version on HuggingFace or Streamlit Cloud

Acknowledgements
Built by Bhargav Gajjala
Inspired by agent-based design, LangGraph, and the power of structured AI reasoning.


import streamlit as st
from main import graph

st.set_page_config(page_title="SkillBuilder AI", layout="centered")

st.title(" SkillBuilder AI")
st.subheader("Create your personalized learning roadmap")

st.markdown(
    """
    This AI assistant helps you build a step-by-step learning plan based on your career goal.
    """
)

# Input box
user_goal = st.text_input(" Enter your career goal", placeholder="e.g., I want to become a Machine Learning Engineer")

if st.button("Generate Learning Path") and user_goal:
    with st.spinner("Thinking..."):
        output = graph.invoke({"input": user_goal})

    st.success("Here's your learning roadmap!")

    st.markdown("### 🔹 Your Goal:")
    st.markdown(f"`{output['input']}`")

    st.markdown("### Milestones:")
    for idx, step in enumerate(output["milestones"], start=1):
        st.markdown(f"{idx}. {step}")

    st.markdown("###  Recommended Resources:")
    for resource in output["resources"]:
        st.markdown(f"- {resource}")

    st.markdown("###  Plan Status:")
    st.code(output.get("status", "Complete"))
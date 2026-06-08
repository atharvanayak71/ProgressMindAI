import streamlit as st
import requests

API_URL = "http://127.0.0.1:8080"

st.set_page_config(page_title="ProgressMind", page_icon="🧠")

page = st.sidebar.selectbox("Navigate", ["🌅 Morning Planner", "🌙 Evening Review"])

if page == "🌅 Morning Planner":
    st.title("🌅 Morning Planner")
    st.write("Tell me about your day and I'll create a personalized plan.")

    tasks = st.text_area("📋 Tasks", placeholder="Enter each task on a new line")
    goals = st.text_area("🎯 Goals", placeholder="Enter each goal on a new line")
    blockers = st.text_area("🚧 Blockers", placeholder="Enter each blocker on a new line")

    if st.button("Generate My Plan ✨"):
        if not tasks:
            st.error("Please enter at least one task.")
        else:
            with st.spinner("ProgressMind is thinking..."):
                response = requests.post(f"{API_URL}/morning-plan", json={
                    "tasks": tasks.strip().split("\n"),
                    "goals": goals.strip().split("\n"),
                    "blockers": blockers.strip().split("\n")
                })

                if response.status_code == 200:
                    plan = response.json()["plan"]
                    st.success("Your plan is ready!")
                    st.markdown(plan)
                else:
                    st.error("Something went wrong. Is your backend running?")

elif page == "🌙 Evening Review":
    st.title("🌙 Evening Review")
    st.write("Let's reflect on your day and plan for tomorrow.")

    completed = st.text_area("✅ Completed Tasks", placeholder="Enter each completed task on a new line")
    incomplete = st.text_area("❌ Incomplete Tasks", placeholder="Enter each incomplete task on a new line")
    blockers = st.text_area("🚧 New Blockers", placeholder="Enter each blocker on a new line")
    mood = st.text_input("😊 Mood", placeholder="How are you feeling? e.g. productive, tired, focused")

    if st.button("Review My Day ✨"):
        if not completed:
            st.error("Please enter at least one completed task.")
        else:
            with st.spinner("ProgressMind is analyzing your day..."):
                response = requests.post(f"{API_URL}/evening-review", json={
                    "completed_tasks": completed.strip().split("\n"),
                    "incomplete_tasks": incomplete.strip().split("\n"),
                    "new_blockers": blockers.strip().split("\n"),
                    "mood": mood
                })

                if response.status_code == 200:
                    review = response.json()["review"]
                    st.success("Your daily review is ready!")
                    st.markdown(review)
                else:
                    st.error("Something went wrong. Is your backend running?")
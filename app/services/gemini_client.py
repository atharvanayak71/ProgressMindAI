import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_morning_plan(tasks: list, goals: list, blockers: list) -> str:
    prompt = f"""
    You are ProgressMind, an AI daily planning assistant.
    
    The user has shared their day with you:
    
    Tasks: {tasks}
    Goals: {goals}
    Blockers: {blockers}
    
    Give them:
    1. A prioritized task order with reasons
    2. How to execute each task
    3. Practical tips for productivity
    4. How to overcome each blocker
    
    Be concise, friendly, and actionable.
    """
    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )

    return response.choices[0].message.content

def get_evening_review(completed_tasks: list, incomplete_tasks: list, new_blockers: list, mood: str = None) -> str:
    prompt = f"""
    You are an expert productivity coach.
    Analyze the user's day based on the following information:

    Completed Tasks: {completed_tasks}
    Incomplete Tasks: {incomplete_tasks}
    New Blockers: {new_blockers}
    Mood: {mood}

    Provide:
    1. Analysis of completed tasks and productivity patterns
    2. Reasons incomplete tasks may have been missed
    3. Suggestions to overcome the reported blockers
    4. A prioritized plan for tomorrow
    5. One actionable improvement for the next day

    Keep the response practical, concise, and supportive.
    """
    response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )

    return response.choices[0].message.content
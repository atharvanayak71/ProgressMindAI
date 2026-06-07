import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text
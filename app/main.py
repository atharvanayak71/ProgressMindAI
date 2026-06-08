from fastapi import FastAPI
from app.models.schemas import MorningPlanRequest, MorningPlanResponse
from app.models.schemas import EveningReviewRequest, EveningReviewResponse  
from app.services.gemini_client import get_morning_plan, get_evening_review

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status" :  "ProgressMind AI is running"}

@app.post("/morning-plan")
def morning_plan(request: MorningPlanRequest):
    plan = get_morning_plan(request.tasks, request.goals, request.blockers)
    return {"plan": plan}

@app.post("/evening-review")
def evening_review(request: EveningReviewRequest):
    review = get_evening_review(request.completed_tasks, request.incomplete_tasks, request.new_blockers)
    return {"review": review}
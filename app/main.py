from fastapi import FastAPI
from app.models.schemas import MorningPlanRequest, MorningPlanResponse
from app.models.schemas import EveningReviewRequest, EveningReviewResponse
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status" :  "ProgressMind AI is running"}

@app.post("/morning-plan")
def morning_plan(request: MorningPlanRequest):
    return {"message": "Received your plan request", "tasks": request.tasks}

@app.post("/evening-review")
def evening_review(request: EveningReviewRequest):
    return {"status": "Received your review request", "review": request.completed_tasks}
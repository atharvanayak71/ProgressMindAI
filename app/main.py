from fastapi import FastAPI
from app.models.schemas import MorningPlanRequest, MorningPlanResponse
app = FastAPI()

@app.get("/health")
def health_check():
    return {"status" :  "ProgressMind AI is running"}

@app.post("/morning-plan")
def morning_plan(request: MorningPlanRequest):
    return {"message": "Received your plan request", "tasks": request.tasks}
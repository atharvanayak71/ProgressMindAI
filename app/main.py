from fastapi import FastAPI, HTTPException
from app.models.schemas import MorningPlanRequest, MorningPlanResponse
from app.models.schemas import EveningReviewRequest, EveningReviewResponse  
from app.services.ai_client import get_morning_plan, get_evening_review

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status" :  "ProgressMind AI is running"}

@app.post("/morning-plan")
def morning_plan(request: MorningPlanRequest):
    if not request.tasks:
        raise HTTPException(status_code=400, detail="Tasks cannot be empty")
    
    try:
        plan = get_morning_plan(request.tasks, request.goals, request.blockers)
        return {"plan": plan}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")


@app.post("/evening-review")
def evening_review(request: EveningReviewRequest):
    if not request.completed_tasks:
        raise HTTPException(status_code=400, detail="Completed Tasks cannot be empty")
    
    try:
        review = get_evening_review(request.completed_tasks, request.incomplete_tasks, request.new_blockers)
        return {"review": review}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")
    
    
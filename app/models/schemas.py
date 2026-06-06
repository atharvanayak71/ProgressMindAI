from pydantic import BaseModel
from typing import List, Optional

# BaseModel  :- every Pydantic model inherits from this. It gives your class all the validation superpowers.
# List[str] — a list of strings. For example ["task1", "task2"].
# MorningPlanRequest — defines what the user sends in.
# MorningPlanResponse — defines what your API sends back.


class MorningPlanRequest(BaseModel):
    tasks : List[str]
    goals : List[str]
    blockers : List[str]

class MorningPlanResponse(BaseModel):
    prioritized_tasks: List[str]
    execution_guide: str
    tips : str 
    blocker_solutions : str

class EveningReviewRequest(BaseModel):
    completed_tasks: List[str]
    incomplete_tasks: List[str]
    new_blockers: List[str]
    mood: Optional[str] = None # optional — can skip this

class EveningReviewResponse(BaseModel):
    completed_analysis: str
    backlog_plan: str
    blocker_tips: str
    tomorrow_tips: str
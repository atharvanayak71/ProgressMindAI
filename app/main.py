from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status" :  "ProgressMind AI is running"}
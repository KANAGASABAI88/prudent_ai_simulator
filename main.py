from fastapi import FastAPI
from routers import document_classifier

app = FastAPI(title="Prudent AI Backend Simulator")

@app.get("/")
def read_root():
    return {"message": "👋 Welcome to the Prudent AI Simulator API"}


# Register all routers
app.include_router(document_classifier.router)

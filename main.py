from fastapi import FastAPI
from routers import document_classifier

app = FastAPI(title="Prudent AI Backend Simulator")

# Register all routers
app.include_router(document_classifier.router)

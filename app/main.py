from fastapi import FastAPI
from app.api.endpoints import items

app = FastAPI()

@app.get("/")
def read_root():
    return {"FastAPI & Bigquery": "Microservice, Tests: Testing CI/CD using Github Actions"}

app.include_router(items.router, prefix="/items", tags=["items"])

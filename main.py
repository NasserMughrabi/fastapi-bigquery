from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"FastAPI & Bigquery": "Microservice, Testing CI/CD using Github Actions"}


# Code -> Comment -> Test -> Refactor -> Document

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"FastAPI & Bigquery": "Microservice"}


# Code -> Comment -> Test -> Refactor -> Document

from fastapi import FastAPI, HTTPException
import os
from google.cloud import bigquery
from models.itemsModel import Item
from services.itemsService import insert_item, get_items

app = FastAPI()

@app.get("/")
def read_root():
    return {"FastAPI & Bigquery": "Microservice, Tests: Testing CI/CD using Github Actions"}

@app.post("/items")
def create_item(item: Item):
    return insert_item(item)

@app.get("/items")
def retrieve_items():
    return get_items()

# Code -> Comment -> Test -> Refactor -> Document

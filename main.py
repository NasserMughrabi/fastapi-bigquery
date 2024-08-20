from fastapi import FastAPI, HTTPException
import os
from google.cloud import bigquery
from pydantic import BaseModel
from bigquery_utils import create_items_table

app = FastAPI()

# Initialize BigQuery client
client = bigquery.Client()
PROJECT_ID = os.getenv("PROJECT_ID")

@app.get("/")
def read_root():
    return {"FastAPI & Bigquery": "Microservice, Tests: Testing CI/CD using Github Actions"}

# Define the Pydantic model for an item
class Item(BaseModel):
    id: str
    name: str

# Function to add an item to the BigQuery table
def insert_item_to_bigquery(item: Item):
    table_id = f"{PROJECT_ID}.fastapi.items"

    # Create items table if it doesn't exist
    create_items_table(PROJECT_ID)

    rows_to_insert = [
        {
            "id": item.id,
            "name": item.name,
        }
    ]
    errors = client.insert_rows_json(table_id, rows_to_insert)  # Make an API request

    if errors:
        raise HTTPException(status_code=400, detail=f"Failed to insert item: {errors}")
    return {"message": "Item successfully inserted"}

@app.post("/items/")
def create_item(item: Item):
    return insert_item_to_bigquery(item)

@app.get("/items/")
def retrieve_items():
    table_id = "fastapi-bigquery-gcp.fastapi.items"
    
    # SQL query to fetch all items from the table
    query = f"SELECT * FROM `{table_id}`"
    
    try:
        query_job = client.query(query)  # Make an API request
        items = [dict(row) for row in query_job]  # Convert each row to a dictionary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve items: {str(e)}")
    
    return items

# Code -> Comment -> Test -> Refactor -> Document

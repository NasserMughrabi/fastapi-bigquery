from fastapi import FastAPI, HTTPException
import os
from google.cloud import bigquery
from pydantic import BaseModel
from google.cloud import bigquery
from google.api_core.exceptions import NotFound
from app.api.models.item import Item

# Initialize BigQuery client
client = bigquery.Client()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")

# Specify the table ID (project.dataset.table)
table_id = f"{PROJECT_ID}.fastapi.items"

def create_items_table():
    # Check if the table exists
    try:
        client.get_table(table_id)  # Make an API request to check if the table exists
        print(f"Table {table_id} already exists.")
    except NotFound:
        # Define the schema for the table
        schema = [
            bigquery.SchemaField("id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
        ]

        # Define the table with the schema
        table = bigquery.Table(table_id, schema=schema)

        # Create the table in BigQuery
        table = client.create_table(table)
        print(f"Created table {table.table_id} with schema.")
    except Exception as e:
        print(f"Failed to check if table exists: {e}")

# Function to add an item to the BigQuery table
def create_item(item: Item):
    # Create items table if it doesn't exist
    create_items_table()

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

def get_items():
    table_id = f"{PROJECT_ID}.fastapi.items"

    # SQL query to fetch all items from the table
    query = f"SELECT * FROM `{table_id}`"
    
    try:
        query_job = client.query(query)  # Make an API request
        items = [dict(row) for row in query_job]  # Convert each row to a dictionary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve items: {str(e)}")
    
    return items
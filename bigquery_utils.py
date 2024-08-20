from google.cloud import bigquery
from google.api_core.exceptions import NotFound

def create_items_table(PROJECT_ID):
    # Initialize BigQuery client
    client = bigquery.Client()

    # Specify the table ID (project.dataset.table)
    table_id = f"{PROJECT_ID}.fastapi.items"

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

import os

# For duckdb
DB = os.getenv("DB", "duckdb") # Let's say that it's duckdb by default
DUCKDBPATH = os.getenv("DUCKDBPATH")

# for bigquery
BQ_PROJECT_ID = os.getenv("BQ_PROJECT_ID")
BQ_DATASET = os.getenv("BQ_DATASET")
BQ_DATASET_ID = os.getenv("BQ_DATASET_ID")
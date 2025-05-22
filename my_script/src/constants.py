import os

# For duckdb
DB = os.getenv("DB", "duckdb") # Let's say that it's duckdb by default
DUCKDBPATH = os.getenv("DUCKDBPATH")

# for bigquery
BQ_PROJECT_ID = os.getenv("BQ_PROJECT_ID")
BQ_TABLE1 = os.getenv("BQ_TABLE1")
BQ_TABLE2 = os.getenv("BQ_TABLE2")
# The syntax is not the same for duckdb and bigquery
different_from_syntax = "is distinct from" if DB == "duckdb" else "!="
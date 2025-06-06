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


#select = f"t1.{pk}," + ",".join([f"case when t1.{column} {different_from_syntax} t2.{column} then concat('{{\"', '{column}\":', '[\"', t1.{column}, '\", \"' , t2.{column}, '\"]}}') else null end as diff" for column in column_list if column not in column_to_ignore and column != pk])

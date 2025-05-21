import duckdb

from ..constants import DUCKDBPATH

def get_db_result_duck(request: str) -> list:
    try:
        with duckdb.connect(DUCKDBPATH) as con:
            result = con.execute(request).fetchall()
            return result
    except Exception as e:
        print(f"Error: {e}")
        exit(84)


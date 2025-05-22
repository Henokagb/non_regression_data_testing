from google.cloud import bigquery
from ..constants import BQ_PROJECT_ID


# I could'nt test this part because bigquery free tier doesn't allow inserting data in table


def get_db_result_bq(request: str) -> list:
    client = bigquery.Client(project=BQ_PROJECT_ID)
    try:
        query_job = client.query(request)
        result = query_job.result()
        return result
    except Exception as e:
        print(f"Error: {e}")
        exit(84)

from ..constants import DB, DUCKDBPATH, BQ_PROJECT_ID
from .duckdb_utils import get_db_result_duck
from .bigquery_utils import get_db_result_bq

def send_query(request: str) -> list:
    if DB == "duckdb":
        return get_db_result_duck(request)
    elif DB == "bigquery":
        return get_db_result_bq(request)
    else:
        print("DB not supported")
        exit(84)

def get_columns(table) -> list:
    match DB:
        case "duckdb":
            columns = get_db_result_duck(f"SELECT name FROM pragma_table_info('{table}');")
            return [col[0] for col in columns]
        case "bigquery":
            print("BigQuery is not supported yet")
            exit(84)
            #columns = get_db_result_bq(f"SELECT column_name FROM `{BQ_PROJECT_ID}.{table}`.INFORMATION_SCHEMA.COLUMNS") 


def get_data(table1: str, table2 :str, limit :int=None, pk:str = "id", column_to_ignore:list = []) -> list:
    
    # I Get and check Column list
    column_list = get_columns(table1)
    if column_list != get_columns(table2):
        print("The columns are not the same")
        exit(84)


    # The syntax is not the same for duckdb and bigquery
    different_from_syntax = "is distinct from" if DB == "duckdb" else "!="
    # limit
    limit_part = f"limit {limit}" if limit else ""
    
    # I select only the columns that have differences
    select = f"t1.{pk}," + ",".join([f"case when t1.{column} {different_from_syntax} t2.{column} then concat('{{\"', '{column}\":', '[\"', t1.{column}, '\", \"' , t2.{column}, '\"]}}') else null end as diff" for column in column_list if column not in column_to_ignore and column != pk])

    # Example of the select: 5, '{"last_seen_at":["2024-02-10 09:10:00", "2024-02-10 09:00:00"]}'
    
    where = " or ".join([f"t1.{column} {different_from_syntax} t2.{column}" for column in column_list if column not in column_to_ignore and column != pk])

    request = f"select {select} from {table1} as t1 join {table2} as t2 using({pk}) where {where} {limit_part}"
    result = send_query(request)

    # The result is a list of tuples
    # first, I transform it into a list of lists
    # second, I remove the Nones
    result = [[data for data in rows if data] for rows in result]
    

    return result
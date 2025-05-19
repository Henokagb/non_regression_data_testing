from ..constants import DB, DUCKDBPATH
from .duckdb_utils import get_db_result

def get_columns(table) -> list:
    match DB:
        case "duckdb":
            columns = get_db_result(f"SELECT name FROM pragma_table_info('{table}');")
            return [col[0] for col in columns]


def get_diff(table1: str, table2 :str, column_to_ignore:list = [], pk:str = "id"):
    column_list = []
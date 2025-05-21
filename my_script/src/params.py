from pydantic import BaseModel
from typing import Optional
import argparse


class param_list(BaseModel):
    t1: str
    t2: str
    limit: Optional[int] = None
    pk_cols: Optional[str] = None
    ignore_cols: Optional[str] = None

def get_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("t1", type=str)
    parser.add_argument("t2", type=str)
    parser.add_argument("--limit", type=int, required=False)
    parser.add_argument("--pk-cols", type=str, required=False)
    parser.add_argument("--ignore-cols", type=str, required=False)
    
    args = vars(parser.parse_args())
    
    return args

def is_valid_args(args) -> bool:

    try:
        param_list(**args)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
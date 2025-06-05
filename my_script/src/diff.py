import json

def get_diff(rows:list) -> dict:
    diff_r = {"id": None, "diffs": {}}
    for r in rows[1:]:
        r = r.replace('""', '"null"')
        diff_r["id"] = rows[0]
        diff_r["diffs"].update(json.loads(r))

    return diff_r

def construct_output(result: list) -> str:
    diff_list = []

    for diff in result:
        diff_list.append(get_diff(diff))
    
    # I transform each diff dict into a string
    diff_list = [json.dumps(diff) for diff in diff_list if diff["id"] is not None]
    
    return "\n".join(diff_list)
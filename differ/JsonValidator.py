import json


def is_valid_json(json_str: str) -> bool:
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        return False
    return True

from src.models.validator import function_definition
from src.models.validator import prompt
import json


def load_func_def(path: str):
    """ we will use the utf-8 after"""
    try:
        with open(path, "r", encoding="utf-16") as func:
            data = json.load(func)
        return [function_definition(**element) for element in data]
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON :{path}")
    except FileNotFoundError:
        raise RuntimeError(f"Not Found: {path}")


def loading_prompts(path: str):
    try:
        with open(path, "r", encoding="utf-16") as f:
            data = json.load(f)
        return [prompt(**item) for item in data]
    except FileNotFoundError:
        raise RuntimeError(f"file not found: {path}")
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON in {path}")
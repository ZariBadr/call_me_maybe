from models.validator import function_definition
import json


def load_func_def(path: str):
    try:
        with open(path, "r", encoding="utf-16") as func:
            data = json.load(func)
        return [function_definition(**element) for element in data]
    except json.JSONDecodeError:
        raise RuntimeError(f"Invalid JSON :{path}")
    except FileNotFoundError:
        raise RuntimeError(f"Not Found: {path}")
    
function = load_func_def("data/input/function_definitions.json")
for f in function:
    print(f"{f} \n")
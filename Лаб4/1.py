# TODO решите задачу
import json

file = "input.json"


def task(filename: str) -> float:
    with open(file, "r", encoding='utf-8') as f:
        data = json.load(f)
        result = sum(item['score'] * item['weight'] for item in data)
    return round(result, 3)


print(task(file))

from os import path
import json

filename = path.join(path.dirname(__file__), "number.json")
with open(filename) as f:
    numbers = json.load(f)
print(numbers)


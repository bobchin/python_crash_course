from os import path
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = path.join(path.dirname(__file__), "number.json")
with open(filename, 'w') as f:
    json.dump(numbers, f)

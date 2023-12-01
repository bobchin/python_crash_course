from os import path
import json

filename = path.join(path.dirname(__file__), "username.json")
with open(filename) as f:
    username = json.load(f)
    print(f"おかえりなさい、{username}さん！")


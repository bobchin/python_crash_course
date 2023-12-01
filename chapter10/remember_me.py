from os import path
import json

username = input("あなたのお名前は？ ")

filename = path.join(path.dirname(__file__), "username.json")
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"戻ったときにも名前をおぼえていますよ、{username}さん！")


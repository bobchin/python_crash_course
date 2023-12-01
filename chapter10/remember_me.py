from os import path
import json


filename = path.join(path.dirname(__file__), "username.json")
try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("あなたのお名前は？ ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"戻ったときにも名前をおぼえていますよ、{username}さん！")
else:
    print(f"おかえりなさい、{username}さん！")

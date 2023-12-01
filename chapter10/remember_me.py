from os import path
import json

def fullpath(filename):
    return path.join(path.dirname(__file__), filename)

def get_stored_username():
    """保存されたユーザ名があれば取得する"""
    filename = fullpath("username.json")
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """新たなユーザ名の入力を促す。"""
    username = get_stored_username()
    if username:
        print(f"おかえりなさい、{username}さん！")
    else:
        username = input("あなたのお名前は？ ")
        filename = fullpath("username.json")
        with open(filename, 'w') as f:
            json.dump(username, f)
    return username

def greet_user():
    """ユーザ名であいさつする。"""
    username = get_stored_username()
    if username:
        print(f"おかえりなさい、{username}さん！")
    else:
        username = get_new_username()
        print(f"戻ったときにも名前をおぼえていますよ、{username}さん！")


greet_user()
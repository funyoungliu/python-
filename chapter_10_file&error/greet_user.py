import json

filename = 'username.json'
#加载json文件
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

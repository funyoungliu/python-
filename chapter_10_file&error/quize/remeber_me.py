import json
def get_sorted_user():
    """如果存储了用户，就获取它"""
    filename='files/username.json'
    try:
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """提示用户输入用户名"""
    username=input('你的名字是什么？')
    filename='username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    username=get_sorted_user()
    if username:
        print('你好，'+username+'!')
    else:
        username=get_new_username()
        print('我们记住你了，'+username,'!')
greet_user()
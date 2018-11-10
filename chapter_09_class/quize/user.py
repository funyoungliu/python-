class User():
    """一个用户描述"""
    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.login_attempts=0
    def describe_user(self):
        print('这个人的名字是：'+self.first_name+self.last_name)
        print('年龄：'+str(self.age))
        print('性别：'+self.gender)
    def get_user(self):
        print('你好，'+self.first_name+self.last_name)
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0

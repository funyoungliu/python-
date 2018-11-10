from user import User
class Privileges():
    """一个权限类"""
    def __init__(self):
        self.privileges=[
            'can add post',
            'can delete post',
            'can ban user',
        ]
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)
class Admin(User):
    """一个管理用户的简单描述"""
    def __init__(self,first_name,last_name,age,gender):
        super().__init__(first_name,last_name,age,gender)
        self.privileges=Privileges()
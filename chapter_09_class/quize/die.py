from random import randint
class Die():
    """一个多面骰子类"""
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
         print(randint(1,self.sides))
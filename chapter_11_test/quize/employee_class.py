class Employee():
    def __init__(self,name,age,wage):
        self.name=name
        self.age=age
        self.wage=wage
    def give_raise(self,add=5000):
        self.wage+=add
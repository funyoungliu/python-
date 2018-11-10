class Restaurant():
    """一家餐馆的简单描述"""
    def __init__(self,name,type):
        self.restaurant_name=name
        self.cuisine_type=type
        self.number_served=0
    def describe_restaurant(self):
        print('这家餐馆的名字是：'+self.restaurant_name+'，这家餐馆的类型是：'+self.cuisine_type)
    def open_restaurant(self):
        print('这家餐馆正在营业')
    def set_number_served(self,number):
        self.number_served=number
    def increment_number_served(self,addnumber):
        self.number_served+=addnumber
class IceCreamStand(Restaurant):
    """一家冰淇淋店的简单描述"""
    def __init__(self,name,type):
        super().__init__(name,type)
        self.flavors=['蓝莓冰淇淋','甜筒','草莓冰淇淋','奶油冰淇淋']
    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)

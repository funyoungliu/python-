def cars_info(manufacturer,type,**car_info):
    car={}
    car['manufacturer']=manufacturer
    car['type']=type
    for name,value in car_info.items():
        car[name]=value
    return car
car=cars_info('大众','小轿车',颜色='红色',配件='比亚迪')
for name,infomation in car.items():
    print(name+':'+infomation)
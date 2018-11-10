sandwich_orders=['Salmon','sausage','pastrami','salad','pastrami','lettuce','pastrami']
print('The pastrami sells out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
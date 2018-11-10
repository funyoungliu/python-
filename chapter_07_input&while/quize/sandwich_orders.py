sandwich_orders=['Salmon','sausage','salad','lettuce']
finished_sandwiches=[]
while sandwich_orders:
    current_sandwich=sandwich_orders.pop()
    print(' The '+current_sandwich+' is finished')
    finished_sandwiches.append(current_sandwich)
print('The all sandwiches are finished')
print(sandwich_orders)
print(finished_sandwiches)
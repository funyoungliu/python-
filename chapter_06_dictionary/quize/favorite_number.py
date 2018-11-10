favorite_numbers={
    'shanjianchang':[1,2,3,4],
    'dangguoqing':[2,4,6,8],
    'congkaichi':[1,3,5,7],
    'liufangyan':[5,6,7,8],
    'lindan':[2,10],
    }
for name,values in favorite_numbers.items():
    print('\n'+name+' likes ')
    for value in values:
        print('\n'+str(value))
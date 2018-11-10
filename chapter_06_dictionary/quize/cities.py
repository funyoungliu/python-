cities={
    'beijing':{
        'country':'China',
        'population':'1400万',
        'fact':'拥挤'
        },
    'newyork':{
        'country':'Us',
        'population':'1200万',
        'fact':'时尚'
        },
    'paris':{
        'country':'France',
        'population':'500万',
        'fact':'浪漫'
        },
    }
for city,values in cities.items():
    print('\n'+city)
    for information,value in values.items():
        print('The '+information+' is:')
        print(value)
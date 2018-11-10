rivers={
    'nile':'egypt',
    '黄河':'中国',
    '恒河':'印度',
    }
for river,country in rivers.items():
    print('The '+river+' runs through '+country)
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
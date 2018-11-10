import json
filename='files/number.json'
number=input('你最喜欢的数字是：')
with open(filename,'w') as favorite_number:
    json.dump(number,favorite_number)
try:
    with open(filename) as favorite_number:
        contents=json.load(favorite_number)
except FileNotFoundError:
    print('你还没有输入喜欢的数字')
else:
    print('我知道你最喜欢的数字是：'+contents)
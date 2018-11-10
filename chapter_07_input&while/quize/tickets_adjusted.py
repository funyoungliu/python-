promat='please input your age'
promat+='\n:'
age=''
active=True
while active:
    age=input(promat)
    if age=='quit':
        active=False
    elif int(age)<=3:
        print('you are free')
    elif 3<int(age)<=12:
        print('your price is 10 dollar')
    elif 12<int(age):
        print('your price is 15 dollar')
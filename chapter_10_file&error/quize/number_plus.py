def number_plus(number_1,number_2):
    number=number_1+number_2
    return number
promat_1='请输入一个数字：'
promat_1+="\n（如果退出请按'q'）"
promat_2='请输入下一个数字：'
promat_2+="\n（如果退出请按'q'）"
while True:
    active=True
    while active:
        number_1=input(promat_1)
        if number_1=='q':
            break
        try:
            number_1=int(number_1)
        except ValueError:
            print('对不起，您输入的不是一个数字')
        else:
            active=False
    if number_1=='q':
        break
    active=True
    while active:
        number_2=input(promat_2)
        if number_2=='q':
            break
        try:
            number_2=int(number_2)
        except ValueError:
            print('对不起，您输入的不是一个数字')
        else:
            active=False
    if number_2=='q':
        break
    num=number_plus(number_1,number_2)
    print(num)
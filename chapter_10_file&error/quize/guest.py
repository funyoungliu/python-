filename='files/guest.txt'
guest_message=''
while guest_message!='q':
    promat='请输入你的名字：'
    promat+="\n（如果退出请按'q'）"
    guest_message=input(promat)
    with open(filename,'a',encoding='UTF-8') as file_object:
        if(guest_message!='q'):
            file_object.write('\n'+guest_message)
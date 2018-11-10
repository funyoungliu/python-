filename='files/Tom pagdin.txt'
try:
    with open(filename,encoding='UTF-8') as Tom_Pagdin:
        contents=Tom_Pagdin.read()
except FileNotFoundError:
    print('没有'+filename+'这个文件')
else:
    num_the=contents.lower().count('the')
    print('这本书一共有'+str(num_the)+'个the')
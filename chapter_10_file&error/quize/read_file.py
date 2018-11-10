filename='files/python学习笔记.txt'
with open(filename,encoding='UTF-8') as file_object:
    contents=file_object.read()
    print(contents)
with open(filename,encoding='UTF-8') as file_object:
    for line in file_object:
        line=line.replace('python','c')
        print(line.rstrip())
with open(filename,encoding='UTF-8') as file_object:
    lines=file_object.readlines()
    for line in lines:
        print(line.rstrip())
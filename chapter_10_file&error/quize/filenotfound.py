filename_cat='files/cats'
filename_dog='files/dogs.txt'
try:
    with open(filename_cat,encoding='UTF-8') as cats:
        contents=cats.read()
except FileNotFoundError:
    #print('没有'+'filename-cat'+'这个文件')
    pass
else:
     print(contents)
try:
    with open(filename_dog,encoding='UTF-8') as dogs:
        contents=dogs.read()
except FileNotFoundError:
    #print('没有'+'filename-dog'+'这个文件')
    pass
else:
     print(contents)
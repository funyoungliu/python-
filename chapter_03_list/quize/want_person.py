persons=['yangyanling','liuhongtao','xixiaowen','lidanyang']
massage='I would like to dinner with '
print(massage)
print(persons)
notcome=persons[2]+' is too busy to come'
print(notcome)
del persons[2]
print(massage)
print(persons)
print('I find a bigger table,so,'+massage)
persons.append('shanjianchang')
persons.append('congkaichi')
persons.insert(0,'dangguoqing')
print(persons)
print('the table will not come')
massage='I am sorry, '
names=persons.pop()
print(massage+names)
names=persons.pop()
print(massage+names)
names=persons.pop()
print(massage+names)
names=persons.pop()
print(massage+names)
print("I would like dinner with")
print(persons)
del persons[0]
del persons[1]
print(persons)
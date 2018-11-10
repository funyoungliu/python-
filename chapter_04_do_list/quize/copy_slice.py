pizzas=['xiangchang','naiyou','gali','mala','xiangla']
friend_pizzas=pizzas[:]
pizzas.append('aoerliang')
friend_pizzas.append('jichi')
print('My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
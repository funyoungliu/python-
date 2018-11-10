#列表副本
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 
#添加元素
my_foods.append('cannoli') 
friend_foods.append('ice cream') 
#查看原列表是否变了
print("My favorite foods are:")
print(my_foods)
#打印列表副本
print("\nMy friend's favorite foods are:")
print(friend_foods)

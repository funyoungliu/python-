promat_name="what's your name:"
promat_place='If you could visit one place in the world,where would you go'
active=True
favorite_place={}
while active:
    name=input(promat_name)
    place=input(promat_place)
    favorite_place[name]=place
    massage=input('There are people?')
    if massage.lower()=='no':
        active=False
for name,place in favorite_place.items():
    print('The '+name+' likes '+place)
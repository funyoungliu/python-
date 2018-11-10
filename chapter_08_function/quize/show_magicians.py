def show_magicians(magicians):
    for magician in magicians:
        print(magician)
def make_great(magicians):
    for number in range(1,len(magicians)+1):
        magicians[number-1]='The Great '+magicians[number-1]
    return magicians
magicians=['liuqian','david','liufangyan','shanjianchang']
magicians_adjusted=make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_adjusted)
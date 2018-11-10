favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
names=['jen','shanjianchang','dangguoqing','sarah']
for name in names:
    if name in favorite_languages.keys():
        print('Thank you '+name)
    else:
        print('please '+name)
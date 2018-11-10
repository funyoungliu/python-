favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
#遍历字典键和键值
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

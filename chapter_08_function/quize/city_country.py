def city_country(city,country='china'):
    """返回城市及其所属国家"""
    message=city.title()+','+country.title()
    return message
text=city_country('santiago','chile')
print(text)
text=city_country('beijing')
print(text)
text=city_country('shanghai')
print(text)
def city_country(city,country,population=0):
    """描述一个城市及其所在国家"""
    if population==0:
        message=city.title()+','+country.title()
    else:
        message=city.title()+','+country.title()+' - population '+str(population)
    return message
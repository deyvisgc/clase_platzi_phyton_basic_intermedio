
def get_population(country_selected):
    # keys=['col', 'bol']
    # values = [300, 400]
    # return keys, values
     #forma one
    #  population_fields = {}
    #  for item in country_selected:
    #     for key, value in item.items():
    #         print(key.lower())
    #         if 'population' in key.lower(): 
    #            population_fields[key] = value
    #         # print(value)
    # #         if 'population' in key.lower():
    # #             population_fields[key] = value

    #  print(population_fields)
    # forma two
    # item[0].lower() => aqui hago referencia al key


    population_fields = dict(filter(lambda item: 'population' in item[0].lower(), country_selected[0].items()))
    # number_v3 = list(map(converNumber, population_fields))  population_fields.values()
    labels = population_fields.keys()
    values = list(map(lambda x: int(float(x)), population_fields.values()))
    return labels, values
def population_by_country(data, country):
    # result = list(filter(lambda c: c["country"] == country, data))
    # return result
    country_selected = list(filter(lambda x: x['Country/Territory'] == country, data))
    return country_selected
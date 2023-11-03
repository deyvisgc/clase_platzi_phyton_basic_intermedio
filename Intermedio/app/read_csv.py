import csv

def read_csv(path: str):
    with open(path, 'r') as file:
      reader = csv.reader(file, delimiter=',')
      header = next(reader) # obtengo la primera fila para obtener los nombres del excel
      population = []
      for row in reader:
         # el zip sirve para unir arrays aqui estoy union la cabecera con las columnas
         # El zip devuelve un array de tuplas
        #  print('****' * 6)
         iterable = zip(header, row) 
         #convierto el array de tuplas en una lista
         #print(list(iterable))
        #conviero el array de tuplas en un diccionario utilizando dictionary_comprehension.py
         country_dict = {key: val for key, val in iterable}
         convert_dict = dict(country_dict)
         population.append(convert_dict)
        #  print(convert_dict.popitem("Vanuatu"))
    return population
if __name__ == '__main__': # esto sirve para correr como un scrpt las funciones
 data = read_csv('./public/world_population.csv')
 country_selected = list(filter(lambda x: x['Country/Territory'] == 'Albania', data))
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
#forma two
#item[0].lower() => aqui hago referencia al key
# population_fields = dict(filter(lambda item: 'population' in item[0].lower(), country_selected[0].items()))
# values = list(population_fields.values())
# print(values)
# result = list(map(lambda x: int(float(x)), values))
# print(result)
#  print(population_fields)
#  print(country_selected)
#  win_team = list(filter(lambda x: x['home_team_result'] == 'Win', matches))
# print(win_team)


    # with open(path, 'r') as csvfile:      
    #   total = sum(int(r[1]) for r in csv.reader(csvfile))
    #   return total
#  print(data[1])

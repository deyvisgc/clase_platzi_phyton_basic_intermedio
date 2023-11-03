import random
dict = {}
#creo clave y valor
'''
Clave : dict[i]
Valor: i * 2
'''
for i in range(1, 11):
    dict[i] = i * 2
#print(dict)
#diccionaru comprehension
dict2 = {i: i * 2 for i in range(1, 11) }
#print(dict2)

countries = ['col', 'mex', 'pe']
population = {}
dict_names = {}
for c in countries:
    population[c] = random.randint(1, 100)
# print (population)
#diccionaru comprehension
population_v2 = {i: random.randint(1, 100) for i in countries}
# print(population_v2)
names=['deyvis', 'lesly', 'ronald']
ages=[20, 21, 23]
# Une las listas, esto se convierte en tuplas
#print(list(zip(names, ages)))
# como esta en tuplas obtengo key y value
# Zip sirve para unir 2 listas y convertirlos en tuplas
for (name, age) in zip(names, ages):
     dict_names[name] = age
print(dict_names)
#diccionaru comprehension
dict_names_v2 = { name: age for(name, age) in zip(names, ages)}
print(dict_names_v2)
import random
countries = ['col', 'bol', 'per']

populations = {country: random.randint(1, 100) for country in countries}
print(populations)

result = { country: population for (country, population) in populations.items() if population > 50}
print(result)

text = 'Hola, soy deyvis'
#el valor es el total de veces que se repite cada letra
unique = { c: text.count(c) for c in text if c in 'aeiou' }
print(unique)
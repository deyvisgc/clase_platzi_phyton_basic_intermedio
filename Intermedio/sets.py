#sets(conjuntos) no permiten valores duplicado y el orden no existe
set_countries = {'col', 'mex', 'bol', 'bol'}
'''
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 445, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.2}
print(set_types)
set_from_string = set("hola") # esto lo separa por caracter, esto no agarra caracter duplicados
print(set_from_string)

set_from_tuples  = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)
numbers = [1,2,3, 1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
#convertir set a listas
unique_numbers = list(numbers)
print(unique_numbers)
'''
set_numbers = {1, 2, 3, 445, 23}
print(len(set_numbers))
a = {1,2}
b = {2,3}
print(a & b)
print(0/0)
# modificando conjuntos
# ¿Cuál será el resultado del siguiente bloque de código?

# a = {1,2}
# b = {2,3}
# print(a & b)
#  result {2}

# ¿Cuál será el resultado del siguiente bloque de código?

# a = {1,2}
# b = {2,3}
# print(a & b)
# debe ser lista(map)
# .
# ¿Cuál es la principal característica de una función Lambda o anónima?
#respuesta erronea = Que no hace falta invocarlas para ser utilizadas.
# respuesta ok =  solo pueden contener una expresión
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}
###############union de conjuntos################
#con metodos
set_c = set_a.union(set_b)
print(set_c)
#con operadores matematico
print(set_a | set_b)

###############insetecepcion de conjuntos################
#con metodos
set_c = set_a.intersection(set_b)
print(set_c)
#con operadores matematico
print(set_a & set_b)

###############diferencia de conjuntos################
#con metodos
set_c = set_a.difference(set_b)
print(set_c)
#con operadores matematico
print(set_a - set_b)
###############symmetric_difference de conjuntos################
# muestra todos los valores que no se repiten en ambos conjuntos
#con metodos
set_c = set_a.symmetric_difference(set_b)
print(set_c)
#con operadores matematico
print(set_a ^ set_b)
###############copiar conjuntos################
set_numbers={1, 2, 3, 4}
set_numbersv1 = set_numbers.copy()
print(set_numbersv1)
###############issuperset################
# va salir true si existen todos los valores del conjunto y
# en x caso contrario saldra false
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "d"}
z = x.issuperset(y) 
print(z)
# soluccion:
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
#new_set = countries.union(northAm).union(centralAm).union(southAm)
new_set = countries.union(northAm, centralAm, southAm)
print(new_set)
# Escribe tu solución 👇

#print(new_set)

#metoh conjuntos: https://www.w3schools.com/python/python_ref_set.asp


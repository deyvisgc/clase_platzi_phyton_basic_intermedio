set_countries = {'col', 'mex', 'pe'}
size = len(set_countries)
print(size)

#agregar
set_countries.add('par')
print(set_countries)
# no registra repetidos los conjuntos
set_countries.add('par')
print(set_countries)
#update
set_countries.update({'col', 'pe', 'ven'})
print(set_countries)
#remove
# elimina siempre cuando existe el valor que se envia si no te envia error

set_countries.remove('ven')
print(set_countries)
# elimina si encuentra si no encuentra no hace nada no te manda error
set_countries.discard('par')
print(set_countries)
# si se quiere eliminar todo el conjunto
print(set_countries.clear())
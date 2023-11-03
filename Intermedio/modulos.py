import sys # este modulos nos da las propiedades del lugar donde se ejecuta
print(sys.path)
import re # este modulo es para aplicar expreciones regulares
text = "Mi numero de telefono es 931 091 443, el codigo del pais es 51, mi numero de la suerte es 13"
# obtener solo los string que contengan numeros
#[0-9] => obtengo los numeros enteros
# + => que me obtenga los numeros completos
result = re.findall('[0-9]+', text)
print("Numeros: ", result)

import time
timestamp = time.time()
local = time.asctime(time.localtime())
print(timestamp) # formato binario
print(local)     # formato humano
import collections
numbers = [1,2,3,54,5,2,3,2,3,23,2,4]
counter = collections.Counter(numbers) # obtengo el total de repeticiones de cada item de la lista
print(counter)

#############################Crear modulos Propios###################################

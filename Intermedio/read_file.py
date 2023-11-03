file = open('./public/prueba.txt')
# print(file.read()) # leero todo el archivo
# print(file.readline()) # leer linea a linea
# print(file.readline()) # leer linea a linea
# print(file.readline()) # leer linea a linea
# print(file.readline()) # leer linea a linea
# cerrar el archivo esto  puedo ayudar a liberar espacion en memoria en phyton
# for line in file:
#     print(line)
#     print(line.replace("line2", "gikss"))
# file.close()
# Este codigo cierra el archivo sin la necesidad de agrefar el file.close
with open('./public/prueba.txt') as file:
    for line in file:
        print(line)
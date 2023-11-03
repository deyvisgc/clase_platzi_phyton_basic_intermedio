#permisos de lectura de archivo: r
# permiso de escritura de archivo: w
# ambos permisos: r+ agrega las nuevas scrituras a las ya existentes
# ambos permisos: w+ remplaza la totalida de la escritura del archivo
#cada linea se aagrega al final de cada linea
# with open('./public/prueba.txt', 'r+')  as file:
#     for line in file:
#         print(line)
#     file.write("nuevas cosas en el archivos")   ## esto escribe sin el salto de linea
#     file.write("otra linea\n")## esto escribe con el salto de linea
#     file.write("mas linea\n")## esto escribe con el salto de linea

with open('./public/prueba.txt', 'w+')  as file:
    for line in file:
        print(line)
    file.write("esta informacion remplazara a lo anterior en totalidad\n")   ## esto escribe sin el salto de linea
    file.write("otra linea1\n")## esto escribe con el salto de linea
    file.write("mas linea2\n")## esto escribe con el salto de linea    
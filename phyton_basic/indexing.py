texto= "Ella sabe python"
print(texto[0])
print(texto[1])
# obtener el ultimo index formula 1
size = len(texto)
print(texto[size - 1])
# obtener el ultimo index formula 2
print(texto[-1]) # con esto lo decimos que se empieze a contar desde el ultimo

# slicing => 
# obtengo las letras de acuerdo a un rango funciona como substring
print(texto[0:5])
print(texto[10:16])
# cuando no le pones el numero inicial python por defecto agarra la posicion inicial
print(texto[:10])
print(texto[5:-1])
# cuando no le pones el numero final python por defecto agarra la posicion final
print(texto[5:])
# cuando no le pones el numero inicial ni final python por defecto agarra todos los caracteres
print(texto[:])

# saltos para sacar textos
# primer parametro => numero inicial
# segundo parametro => numero final
# tercer parametro => numero de saltos
# el numero de saltos se cuenta desde el caracter donde empieza
print(texto[10:16: 1])
print(texto[10:16: 2])
print(texto[::2])
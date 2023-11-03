x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)
#comparar como string
y_str = format(y, ".2g") # le dijo que quiero 2 digitos
print("str => ", y_str)
print(y_str == str(x))

print('*' * 20)
# comprar con entero
tolerancia = 0.00001 # margen tolerancia
# valor absoluto
print(abs(x - y) < tolerancia)

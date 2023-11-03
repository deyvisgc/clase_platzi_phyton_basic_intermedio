numbers = [1, 2, 3, 4]
print(numbers)
'''
numbers[0] = 23 # modificando
print(numbers)
numbers[0] = 1
print(numbers)
numbers.append(5)
print(numbers)
#buscar dentro de una lista
task = ["programar", "documentar"]
# seleccionar partes del array
print(numbers[:3])
print('programar' in task)
'''
# Metodos de listas
# CRUD

# crear
numbers = [1, 2, 3, 4]
#agrego en la ultima posicion
numbers[-1] = 10
#agrego en la ultima posicion
numbers.append(11)
print(numbers)
numbers.insert(2, 6)
print(numbers)
# numbers.reverse()
# obtener valores de acuerdo a su index
# print(numbers.pop(1))
numbers.remove(1)
print(numbers)

#CRUD

numbers = [1, 2, 3, 4, 5]
#read
print(numbers[1])

#update
numbers[-1] = 10 # actualizo el ultimo numero
print(numbers)
#create
# append inserta al ultimo
numbers.append(700)
print(numbers)
# insert => se pasa la posicion y el valor
#python deja insertar tipos diferentes a su array
numbers.insert(1, "change")
print(numbers)

task= ["todo 1", "todo 2", "todo 3"]
new_list= numbers + task # con esto se puede unir listas
print(new_list)

index = task.index("todo 2") # obtener la posicion de un valor en especifico de la lista
new_list[index] = 'todo changed' # actualizo el todo 1
print(new_list)

#delete
new_list.remove("todo 1") # elimina el valor que se agrege en el metodo rempve
print(new_list)

new_list.pop() # elimina el ultimo item de la lista

print(new_list)

new_list.pop(0) # se puede pasar la posicion a eliminar
print(new_list)

new_list.reverse() # cambia el orden de la lista
print(new_list)

numbers_a = [1, 3, 6, 3]
numbers_a.sort() # ordena de menor a mayor numeros

strings = ['re', 'ab', 'ed']
strings.sort() # ordena de acuerdo al abesadario

#Ojo: cuando se tiene un array combinados de numeros y string o tro tipo de dato no funciona este sort








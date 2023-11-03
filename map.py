list_food= ["arroz", "menestra", "jugo"]
numbers= [1, 2, 3, 4]
number_v2= []

for i in numbers:
    number_v2.append(i * 2)
print(number_v2)

# map, map recibe dos parametros, el primero una funcion lamda el segundo el array a iterar
number_v3 = list(map(lambda i: i * 2, numbers))
print(number_v3)

# sumar valores de dos listas
numbers_v1 = [1,2,3,4]
numbers_v2 = [5, 6, 7]
# x = numbers_v1, y = numbers_v2
result = list(map(lambda x, y: x + y, numbers_v1, numbers_v2))
print(result)
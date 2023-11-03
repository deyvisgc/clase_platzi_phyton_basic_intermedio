# def suma(a, b):
#     return a + b
# total = suma(32, 3)
# print(total)
# retornar funciones 
def suma_with_range(ran_in, ran_fin):
    sum = 0
    for x in range(ran_in, ran_fin):
        sum += x
    # print(sum)
    return sum
totalCount = suma_with_range(1, 10)
totalCount2 = suma_with_range(totalCount, totalCount + 10)    
print(totalCount2)

def find_volume(length=1, width=1, depth=1):
    return length * width * depth
result = find_volume(10, 20, 3)
print(result)
#enviar solo las variables que quieras
result1 = find_volume(width=10)
print(result1)

#devolver varios valores => devuelve un tupla
def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'
result2 = find_volume(10, 20, 3)
print(result2)
# obtener multiples valores, cada valor que devuelve se asignara a cada variable que pongas al recibir el retun
result3,width, text  = find_volume(10, 20, 3)
print(result3)
print(width)
print(text)


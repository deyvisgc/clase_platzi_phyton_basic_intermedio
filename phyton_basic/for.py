
#Range crea un rango dado en este ejemplo es del 1 al 21 => solo se pinta del 1 al 20
# for element in range(1, 21):
#     print(element)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in my_list :
    print(i)
my_tupla = ('deyvis', 'ronald', 'lesly')
for j in my_tupla:
    print(j)
product = {
    "name": "tanque rotoplas",
    "price": 700,
    "stock": 80
}
for key in product:
    print(key, " => ", product[key])
# otra forma de iterar product pero mas rapido
# 
for key, value in product.items():
    print(key, "=>", value)



# listas de diccionarios
person = [
    {
        "name": "deyvis",
        "last_name": "garcia cercado",
        "age": 27
    },
    {
        "name": "Lesly",
        "last_name": "Llanos Ponce",
        "age": 26
    },
    {
        "name": "Rocio",
        "last_name": "LLanos Ponce de Garcia",
        "age": 25
    }
]
for per in person:
    print(per.get("name"))
    per.pop("age") # elimini
    #per.update("last_name", "Ponce LLanos")
print(person)

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

# Escribe tu solución 👇

for e in my_list:
  if e > 0 :
      new_list.append(e)

print(new_list)
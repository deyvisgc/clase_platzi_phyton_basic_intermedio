# un diccionario es como hacer un objeto en javascript
person = {
    "name": "deyvis", 
    "lastName": "garcia cercado", 
    "age": 27,
    "lansg": ["python", "javascipt"]
    }
'''
#obtener el tamaño
print(len(my_dict))

# obtener valores primera opcion => para usar esto se debe validar que esa llava exista  si no existe te manda un error
print(my_dict["name"])
# print(my_dict["sasa"])
# obtener valores segunda opcion es la mas adecuada ya que si el key no existe no de manda error
print(my_dict.get("lastName"))
#validar si un key esta o  no en un diccionario
print("name" in my_dict)
print("name1" in my_dict)
'''
#Insertar y actualizar:
print(person)
print("")
person["name"] = 'ronald'
person["lansg"].append("php")
person.setdefault("twiter", "deyvisfdsd")
person["age"] += 20
print(person)
#eliminar
del person["age"]
person.pop("lastName")
print(person)
#al obtener los items te retorna una lista de tuplas de clave y valor
print(person.items())
# Obtener las keys
print(person.keys())
# obtener values
print(person.values())




















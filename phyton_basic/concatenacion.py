
#variables
print("concatenacion")
#input => obtiene el valor desde una consola
name = input("¿ Cual es tu numbre?")
print("")
last_name = input("¿ Cual es tu apellido?")
print("")
age = input("¿ Cual es tu Edad?")
print("")

template = "mi nombre es " + name + " y apellido es: " + last_name, " y mi edad es: " + age + " años"
print("primera cocatenacion ", template)
print("--------------------------------------------")
template = "mi nombre es {} y apellido {} y tengo {} años".format(name, last_name, age)
print("segunda cocatenacion ", template)
print("--------------------------------------------")
template = f"mi nombre es {name} y apellido {last_name} y tengo {age} años"
print("Tercera cocatenacion ", template)



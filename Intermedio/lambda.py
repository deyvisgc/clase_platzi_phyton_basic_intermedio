#funcion normal
def increment(x= 1):
    return x + 1
print(increment(10))
#funcion con lambda
incrementv2 = lambda x : x + 1
result = incrementv2(20)
print(result)

#funcion lambda con 2 parametros:
# title le pongo mayuscula las primera letra de una palabra
# f es para usar parametros en los string sin usar un +
full_lastName = lambda name, last_name : f"Full name is {name.title()} {last_name.title()}"
full = full_lastName("deyvis", "garcia cercado")
print(full)
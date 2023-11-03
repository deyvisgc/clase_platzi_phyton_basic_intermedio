#variables globales y locales
price = 100
# no se puede usar variable globa dentro de una funcion, para que funciona
# en la funcion se debe declarar otra variable dentro de la funcion
# solo se puede usar a fuera de las funciones
# las variables locales solo se pueden usar en la funcion
def incremente():
    price = 0
    price = price + 10 # aqui esta creando una nueva variable tiene otro contexto diferentes, puede tener el mismo nombre
    print(price)
    return price
print(price)    
print(incremente()    )
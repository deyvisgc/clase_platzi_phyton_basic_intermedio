items = [
    {
        'product': "camisa",
        'price': 100
    },
    {
        'product': "pantalones",
        'price': 200
    },
    {
        'product': "corbatas",
        'price': 50
    },
    {
        'product': "zapatos",
        'price': 430
    }
]
items_v1= list(map(lambda x: {"price": x["price"]}, items))
#print(items_v1)
# Map no modifica el array origina si no crea otro array
# cuando se usa diccionario y cambiar el array con un map esto puede cambiar el array original y no crear nuevos array
# Map con funciones => agregar el total del igv a cada item del orden de compras

def add_igv(items):
    # con esto el map ya no modificara el array original,
    # las modificaciones del array original con map solo pasa con dicionarios
    new_items = items.copy()
    new_items['igv'] = new_items['price'] * .19
    return new_items

new_items = list(map(add_igv, items))
print(new_items)
print(items)
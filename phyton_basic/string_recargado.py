text = "Ella sabe promar en python"
'''
# in verifica si una subtexto esta dentro del string
print('Javascript' in text) 
print('python' in text)
if 'python' in text:
    print("Eligiste bien")
else:
    print("Elegiste mal")
 # len cuenta el tamaño de caracteres   
size = len(text)
print(size)
'''
#convierte en mayusculas
print(text, text.upper())
#convierte el primer caracter en mayusculas
print(text, text.capitalize())

#convertir en minuscula
print(text, text.lower())

# contar cuantas veces se repite un caracter en un string
print(text.count("a"))

# convertir al opuesto que esta escrito ejepmlo: si estan en minuscula lo pasa a mayuscula y visebersa
print(text.swapcase())
# encontrar si un texto inicia con un caracter
print(text.startswith("Ella"))
# encontrar si un texto termina con un caracter
print(text.endswith("python"))
#remplazar
print(text.replace("python", "java"))
text_2 = 'esto es un titulo'
print(text_2.capitalize())
# poner las primeras letras del texto en mayusculas
print(text_2.title())
# es numero
print(text.isdigit())
print("1".isdigit())

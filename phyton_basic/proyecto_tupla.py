import random

user_option = input("piedra, papel o tijera: ")
options = ("piedra", "papel", "tijera")
#ramdom recibe una tupla o lista en esta ocaciones su funcion es escojer una de las opciones de la lista
computer_option = random.choice(options)
print("el computador eligio: {}".format(computer_option))

if user_option == computer_option:
  print("empate")
elif user_option == "piedra":
  if computer_option == "tijera":
    print("ganaste")
  else:
    print("perdiste")
elif user_option == "papel":
  if computer_option == "tijera":
    print("perdiste")
  else:
    print("ganaste")
elif user_option == "tijera":
  if computer_option == "papel":
    print("ganaste")
  else:
    print("perdiste")
else:
  print("opción incorrecta")
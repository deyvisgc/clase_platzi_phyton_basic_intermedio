import random
#ramdom recibe una tupla o lista en esta ocaciones su funcion es escojer una de las opciones de la lista
options = ("piedra", "papel", "tijera")
user_wins = 0
computer_wins = 0
rounds = 1
print(int(4.56))
primos = [2,3,5,7,11,13,17,19,23,29,31,37,41]
print(primos[3:10:2]) # el dos quiere decir que va a saltar de dos en dos hasta el 10 para chapar los valores
# print(primos[3])
exit
while True:
    print('*' * 10)
    print('ROUND ', rounds)
    print('*' * 10)
    print("user_wins: ", user_wins)
    print("computer_wins: ", computer_wins)
    user_option = input("piedra, papel o tijera: ")
    computer_option = random.choice(options)
    print("el computador eligio: {}".format(computer_option))
    rounds += 1
    if not user_option in options:
        print("La opcion es incorrecta")
        continue
    if user_option == computer_option:
       print("empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print('piedra gana a tijera')
            print("Usuario gano!")
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print("computadora gano!")
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print("Usuario gano!")
            user_wins += 1
        else:
            print('tijera gana a papel')
            print("computadora gano!")
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print("Usuario gano!")
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print("computadora gano!")
            computer_wins += 1
    if user_wins == 2 :
        print("El ganador es Usuario")
        break
    if  computer_wins == 2:
        print("El ganador es la computadora")
        break
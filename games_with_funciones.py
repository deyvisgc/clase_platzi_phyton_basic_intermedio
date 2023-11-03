import random
def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()
    if not user_option in options:
      print('esa opcion no es valida')
      return None, None
    computer_option = random.choice(options)
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option
def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1
    return  user_wins , computer_wins
def choose_winner(user_wins, computer_wins):
    if computer_wins == 2:
       print('El ganador es la computadora')
       return computer_wins
    #break
    if user_wins == 2:
       print('El ganador es el usuario')
       return user_wins
    #break
def game_rum():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1
        user_option, computer_option = choose_options()
        if user_option == None and computer_option == None :
            continue
        user_wins , computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        winner = choose_winner(user_wins, computer_wins)
        if (winner == 2):
            break
game_rum()        


def message_creator(text):
   # Escribe tu solución 👇

   respuestas = {'computadora' : "Con mi computadora puedo programar usando Python", 
                    'celular' : "En mi celular puedo aprender usando la app de Platzi",
                    'cable' : "¡Hay un cable en mi bota!"}

   if text in respuestas.keys(): 
      return respuestas[text]
   else: 
      return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)
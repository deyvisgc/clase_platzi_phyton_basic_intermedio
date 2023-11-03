items = [
    {
        'product': "tanque rotoplas",
        'price': 200
    },
    {
        'product': "tanque baño",
        'price': 300
    },
    {
        'product': "caños",
        'price': 100
    },
]
new_items = filter(lambda x: x['price'] == 100, items)
print(list(new_items))

#Numeros pares
numbers=[1,2,3,4,5]
new_numbers = filter(lambda n: n % 2 == 0, numbers)
print(list(new_numbers))

# Equipos ganadores

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

win_team = list(filter(lambda x: x['home_team_result'] == 'Win', matches))
print(win_team)






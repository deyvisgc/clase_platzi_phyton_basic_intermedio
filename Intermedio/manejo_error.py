#print(0/0)
# 
'''
sum = lambda x, y : x + y
assert sum(2, 2) == 4
print("suma exitoso")

age = 10
if age < 18:
    raise Exception("no eres mayor de edad")
'''

# try:
#     print(0/0)
# except ZeroDivisionError as error:
#     print(error)
# try:
#     assert 1 != 1, 'Uno no es igual que uno'
# except AssertionError as error:
#     print(error)
# try:
#    age = 10
#    if age < 18:
#     raise Exception("no eres mayor de edad")
# except Exception as error:
#     print(error)
# si ya existe um error ya no continua con los erros si no pasa al siguiente codigo que esta fuera del try except
try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
       raise Exception("no eres mayor de edad")
except ZeroDivisionError as error:
     print(error)
except AssertionError as error:
     print(error)
except Exception as error:
     print(error)          
   
print("continua")    
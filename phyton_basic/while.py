# while True:
#     print("se ejecuto")
# counter = 0
# while counter < 10:
#     counter += 1
#     print("el conter es {}".format(counter))

'''
counter = 0

while counter < 20:
    counter += 1
    # aqui se dice que cuando el valor seha 15 se rompera el bucle
    #break => rompe cualquier iteracion
    if counter == 15:
        break
    print(counter)
'''
counter = 0
while counter < 20:
    counter +=1
    #el continue salta automaticamente al siguiente iteracion obiendo todas las lineas que se encuentran abajo
    if counter < 15:
        continue
    print(counter)


numbers = []
'''
#forma normal
for i in range(1, 11):
   numbers.append(i)
print  (numbers)
#forma con lis comprehension
numbers = [i * 2 for i in range(1, 11)]
print(numbers)
#forma normal
'''

# validando con lis comprehension
for i in range(1, 11):
   if i % 2 == 0:
      numbers.append(i)
print(numbers)
numbers = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers)
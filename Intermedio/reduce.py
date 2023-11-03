import functools
numbers=[1, 2, 3, 4]
total=0
# sumar el array con un for
def accum(counte, item):
    return counte + item

for i in numbers:
    total += i
print(total)
# sumar con redus, counter es el acomulador en otras palabras el contador y el items son los item del array
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)
result_v1 = functools.reduce(accum, numbers)
print(result_v1)
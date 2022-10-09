# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

from random import randint

def List(size, m, n):
    return [randint(m, n) for i in range(size)]

def Value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = List(size, m, n)
print(origin)
print(Value(origin))
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

import math

def is_NaturalN(N):
    natural = [2]
    for num in range(3, N + 1, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            natural.append(num)
    return natural

def get_NaturalN(N, natural):
    fact = []
    for i in natural:
        while N % i == 0:
            N = N / i
            fact.append(i)
    return fact

N = int(input('Введите число: '))

natural = is_NaturalN(N)
factors = get_NaturalN(N, natural)
print(factors)

def test(N, factors):
    return math.prod(factors) == N       

print(test(N, factors))

def NaturalN(N):
    i = 2
    array = []
    while N != 1: 
        if N % i == 0:
            array.append(i) #3
            N = N / i
            i = 2
        else: 
            i += 1
    return (array)

print (NaturalN(5))
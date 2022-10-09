# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
from math import pi

d = pi
print(d)

d = 100
pi_num = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(d))

print(pi_num)

n = 20000000

pi_num = 4 * (sum(1/x for x in range(1, n + 1, 4)) +
             sum(-1/x for x in range(3, n + 1, 4)))

print(format(pi_num, '.100'))
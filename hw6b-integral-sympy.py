from sympy import *

def f(x):
  return 2 * ((4 / (1.2 * sqrt(2 * pi))) * exp(-1 / 2 * ((x - 11) / 1.2) ** 2) + (7 / (2.4 * sqrt(2 * pi))) * exp(-1 / 2 * ((x - 15) / 2.4) ** 2))

x = Symbol('x')

# Невизначений інтеграл
indefinite_integral = integrate(f(x), x)

# Інтеграл від a до b
a = 9
b = 18
definite_integral = integrate(f(x), (x, a, b))

print("Невизначений інтеграл:", indefinite_integral)
print("Інтеграл від", a, "до", b, ":", float(definite_integral))
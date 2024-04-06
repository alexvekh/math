from sympy import Symbol, diff, sqrt

x = Symbol('x')

def func(x):
  return 1/sqrt(x**2 + 1)  # sqrt - функція кореня квадратного

derivative = diff(func(x), x)
print("Похідна:", derivative)

derivative_at_1 = derivative.subs(x, 1)  # Підставити x = 1
derivative_at_minus_half = derivative.subs(x, -1/2)  # Підставити x = -1/2

print("Значення похідної в точці x = 1:", derivative_at_1)
print("Значення похідної в точці x = -1/2:", derivative_at_minus_half)
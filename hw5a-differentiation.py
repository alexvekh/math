import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, symbols

def f(x):
  return x**3 / 3 + x**2 / 2 + 2*x

x_vals = np.linspace(-2, 2, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")

# Дотичні
def f_prime(x):
  return x**2 + x + 2

x, y = symbols('x y')
y = (x**3)/3 + (x**2)/2 + 2*x
dx = diff(y, x)
print("f'(x) = ", dx)

x1 = 1
y1 = f(x1)
f1_prime = f_prime(x1)
print("f'(1) = ", f1_prime)
plt.plot([x1, x1-f1_prime], [y1, y1-f1_prime], color="red", label="f'(1)")

x2 = -1/2
y2 = f(x2)
f2_prime = f_prime(x2)
print("f'(-1/2) = ", f2_prime)
plt.plot([x2, x2-f2_prime], [y2, y2-f2_prime], color="green", label="f'(-1/2)")

plt.legend()
plt.grid()
plt.show()
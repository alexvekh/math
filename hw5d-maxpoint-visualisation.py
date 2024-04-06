import numpy as np
import matplotlib.pyplot as plt

# Функція
def f(x):
  return -3 * x**2 + 30 * x

# Похідна
def f_prime(x):
  return -6 * x + 30

# Точка максимуму
x_maximum = 5
y_maximum = f(x_maximum)

# Діапазон значень x
x_min = -1
x_max = 12

# Обчислення значень y та y'
x = np.linspace(x_min, x_max, 100)
y = f(x)
y_prime = f_prime(x)

# Візуалізація
plt.plot(x, y, label="y = -3x^2 + 30x")
plt.plot(x, y_prime, label="y' = -6x + 30")
plt.scatter(x_maximum, y_maximum, color="red", label="Точка максимуму")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
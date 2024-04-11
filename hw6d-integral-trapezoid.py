from sympy import *
def integrate_trapezoids(f, a, b, n):
  """
  Ця функція використовує метод трапецій для обчислення
  визначеного інтеграла від a до b.

  Args:
      f: Функція, інтеграл якої потрібно обчислити.
      a: Нижня межа інтегрування.
      b: Верхня межа інтегрування.
      n: Кількість підінтервалів.

  Returns:
      Наближене значення визначеного інтеграла.
  """

  h = (b - a) / n
  sum = 0
  for i in range(n+1):
    x_i = a + i * h
    if i == 0 or i == n:
      sum += f(x_i) * h / 2
    else:
      sum += f(x_i) * h

  return sum

# Виконання
def f(x):
  return 2 * ((4 / (1.2 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 11) / 1.2) ** 2) + (7 / (2.4 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 15) / 2.4) ** 2))

a = 9
b = 18
n = 100

integral = integrate_trapezoids(f, a, b, n)

print("Інтеграл методом трапецій:", float(integral))
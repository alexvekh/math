from sympy import *
def integrate_simpson(f, a, b, n):
  """
  Ця функція використовує метод Сімпсона для обчислення
  визначеного інтеграла від a до b.

  Args:
      f: Функція, інтеграл якої потрібно обчислити.
      a: Нижня межа інтегрування.
      b: Верхня межа інтегрування.
      n: Кількість підінтервалів (має бути парним).

  Returns:
      Наближене значення визначеного інтеграла.
  """

  if n % 2 != 0:
    raise ValueError("n має бути парним числом")

  h = (b - a) / n
  sum = 0
  for i in range(n+1):
    x_i = a + i * h
    if i == 0 or i == n:
      sum += f(x_i) * h / 3
    elif i % 2 == 0:
      sum += f(x_i) * 2 * h / 3
    else:
      sum += f(x_i) * 4 * h / 3

  return sum

# Виконанння
def f(x):
  return 2 * ((4 / (1.2 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 11) / 1.2) ** 2) + (7 / (2.4 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 15) / 2.4) ** 2))

a = 9
b = 18
n = 100

integral = integrate_simpson(f, a, b, n)

print("Інтеграл методом Сімпсона:", float(integral))
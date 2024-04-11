from sympy import *
def integrate_rectangles(f, a, b, n):
  """
  Функція використовує метод прямокутників для обчислення визначеного інтеграла від a до b.
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
  for i in range(n):
    x_i = a + i * h + h/2   # +h/2 по середині, +h для правих прямокутників; 0 для лівих
    sum += f(x_i) * h
  return sum

def integrate_rrectangles(f, a, b, n):
  # Обчислення визначеного інтеграла від a до b методом правих прямокутників.
  h = (b - a) / n
  sum = 0
  for i in range(n):
    x_i = a + i * h + h     # для правих прямокутників
    sum += f(x_i) * h
  return sum

def integrate_lrectangles(f, a, b, n):
  # Обчислення визначеного інтеграла від a до b методом лівих прямокутників.
  h = (b - a) / n
  sum = 0
  for i in range(n):
    x_i = a + i * h  #-h для лівих прямокутників
    sum += f(x_i) * h
  return sum


# Виконання
def f(x):
  return 2 * ((4 / (1.2 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 11) / 1.2) ** 2) + (7 / (2.4 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 15) / 2.4) ** 2))

a = 9
b = 18
n = 100

integral = integrate_rectangles(f, a, b, n)
rintegral = integrate_rrectangles(f, a, b, n)
lintegral = integrate_lrectangles(f, a, b, n)

print("Інтеграл методом правих прямокутників:", float(rintegral))
print("Інтеграл методом лівих прямокутників:", float(lintegral))
print("Інтеграл методом середніх прямокутників:", float(integral))
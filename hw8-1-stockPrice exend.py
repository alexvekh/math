"""
Візьми код симуляції із завдання 7 домашнього завдання до теми 7 “Теорія ймовірностей. Комбінаторика”. 
Будемо вважати, що зміна ціни акцій у кожний момент часу дорівнює x ∼ Γ(0.3, 1.1), 
де Г — позначення гамма-розподілу.

Необхідно запустити симуляцію n=100 разів для різних значень часу t.
а) Побудуй гістограму розподілу x.
б) Запусти симуляцію з t від 1 до, наприклад, ~60 з кроком, наприклад, 1 або 2.
Примітка: кінцеве значення t взято умовно рівним 60, але це не відіграє великої ролі, 
головне, щоб воно було достатнім для проходження тесту на нормальність, 
а значення кроку — дозволяло побачити динаміку зміни розподілу. Конкретні значення не так важливі.
Для кожного значення t побудуй гістограму розподілу ціни та перевір його на нормальність. 
Зроби висновки про зміну розподілу зі збільшенням t.
"""

import random
import matplotlib.pyplot as plt
import scipy.stats as stats

def simulate_stock_price(num_simulations, t):
  average_prices = []
  for _ in range(num_simulations):
    price = 0
    for _ in range(t):
      change = stats.gamma.rvs(a=0.3, scale=1.1)  # x ∼ Γ(0.3, 1.1)
      # change = random.choice([2, -1])
      price += change
    # print(price)
    average_prices.append(price/t)
  return average_prices

def plot_histogram(average_prices, num_simulations):
  # гістограма ціни акції.
  plt.hist(average_prices)
  plt.xlabel("Середня ціна акції")
  plt.ylabel("Кількість симуляцій")
  plt.title(f"Гістограма ціни акції (n={num_simulations})")
  plt.show()

# Виконання
num_simulations = 100  # Кількість симуляцій
t_values = list(range(1, 61, 2))  # Значення t (від 1 до 60 з кроком 1)

for t in t_values:
  average_prices = simulate_stock_price(num_simulations, t)
  print(f"Середня ціна акції (t={t}):", sum(average_prices) / len(average_prices))
  # Перевірка на нормальність
  jb_test_result = stats.jarque_bera(average_prices)
  print(f"Тест Jarque-Bera (statistic JB): {jb_test_result[0]:.4f}, (p-value): {jb_test_result[1]:.4f}")
  plot_histogram(average_prices, num_simulations)

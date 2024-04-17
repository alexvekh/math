"""
Ціна акцій компанії в кожен момент часу може з рівною ймовірністю збільшитись на 2 або зменшитись на 1. 
У початковий момент часу t=0 ціна рівна 0. Визнач середню ціну акції через 3 одиниці часу (t=3). 
а) Розв’яжи аналітично. 
б) Напиши симуляцію даного процесу. 
Порахуй середнє значення та намалюй гістограму ціни для 10, 100, 1000 та 10000 симуляцій.
"""

import random
import matplotlib.pyplot as plt

def simulate_stock_price(num_simulations):
  # Симуляція рандомної зміни ціни за 3 часових періода
  average_prices = []

  for _ in range(num_simulations):
    price = 0
    for _ in range(3):
      change = random.choice([2, -1])
      price += change

    average_prices.append(price)

  return average_prices

def plot_histogram(average_prices, num_simulations):
  # гістограма ціни акції.
  plt.hist(average_prices)
  plt.xlabel("Середня ціна акції")
  plt.ylabel("Кількість симуляцій")
  plt.title(f"Гістограма ціни акції (n={num_simulations})")
  plt.show()

# Виконання
num_simulations_list = [10, 100, 1000, 10000]

for num_simulations in num_simulations_list:
  average_prices = simulate_stock_price(num_simulations)
  print(f"Середня ціна акції (n={num_simulations}):", sum(average_prices) / len(average_prices))
  plot_histogram(average_prices, num_simulations)
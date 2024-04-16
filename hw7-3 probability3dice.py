"""
Підкидають три гральні кубики. 
Що ймовірніше: отримати в сумі очок, що випали, 11 або 12? 
Розв’яжи програмно, згенерувавши всі можливі комбінації.
"""


import itertools

import random

def get_sum(dice):
  """Calculates the sum of the dice values."""
  return sum(dice)

# Генерація всіх можливих комбінацій
all_rolls = list(itertools.product(range(1, 7), repeat=3))

# Сортування комбінацій за сумою
all_rolls.sort(key=lambda x: sum(x))

# Виведення комбінацій у форматі "6 комбінацій в рядку"
print("\nМатриця всіх можливих комбінацій (по 6 в рядку):")
for i in range(0, len(all_rolls), 6):  # Групування по 6 елементів
  print(" | ".join(" ".join(str(value) for value in row) for row in all_rolls[i:i+6]))

# Count the number of rolls that sum to 11 and 12
count_11 = 0
count_12 = 0
for roll in all_rolls:
  total = get_sum(roll)
  if total == 11:
    count_11 += 1
  elif total == 12:
    count_12 += 1

# Calculate the probabilities
p_11 = count_11 / len(all_rolls)
p_12 = count_12 / len(all_rolls)
print(f"All rolls: {len(all_rolls)}")
print(f"11 очок: {count_11} rolls")
print(f"12 очок: {count_12} rolls")

# Print the results
print(f"Ймовірність отримати 11 очок: {p_11:.4f}")
print(f"Ймовірність отримати 12 
      очок: {p_12:.4f}")
print('-'*40)
if p_11 == p_12:
  print("Відповідь: Ймовірність однакова.")
elif p_11 > p_12:
  print("Відповідь: Ймовірніше отримати 11 очок.")
else:
  print("Відповідь: Ймовірніше отримати 12 очок.")

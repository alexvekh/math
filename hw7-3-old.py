"""
Підкидають три гральні кубики. Що ймовірніше: отримати в сумі очок, що випали, 11 або 12? 
Розв’яжи програмно, згенерувавши всі можливі комбінації.
"""

import random

def get_sum(dice):
  """Calculates the sum of the dice values."""
  return sum(dice)

# Generate all possible combinations of three dice rolls
all_rolls = []
for i in range(1, 7):
  for j in range(1, 7):
    for k in range(1, 7):
      all_rolls.append((i, j, k))
      print("roll: ", i, j, k)

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
print(f"Ймовірність отримати 12 очок: {p_12:.4f}")
print('-'*40)
if p_11 == p_12:
  print("Відповідь: Ймовірність однакова.")
elif p_11 > p_12:
  print("Відповідь: Ймовірніше отримати 11 очок.")
else:
  print("Відповідь: Ймовірніше отримати 12 очок.")
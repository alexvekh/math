"""
На площині накреслені дві концентричні окружності (мають спільний центр), 
радіуси яких 5 і 10 см відповідно. 
Знайди ймовірність того, що точка, кинута навмання у велике коло, потрапить також 
у кільце, утворене побудованими окружностями. Розв’яжи аналітично.
"""

from numpy import pi
# Площа кола
def s(r):
  return float(pi * r ** 2)

print(f"{s(5):.2f}")
print(f"{s(10):.2f}")
print((314.16 - 78.54) / 314.16)
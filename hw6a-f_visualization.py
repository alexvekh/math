# візуалізація графіку функції
import matplotlib.pyplot as plt
import numpy as np

def np_f(x):
  return 2 * ((4 / (1.2 * np.sqrt(2 * np.pi))) * np.exp(-1 / 2 * ((x - 11) / 1.2) ** 2) + (7 / (2.4 * np.sqrt(2 * np.pi))) * np.exp(-1 / 2 * ((x - 15) / 2.4) ** 2))

x_values = np.linspace(0, 24, 1000)
y_values = np_f(x_values)

plt.plot(x_values, y_values)
plt.xlabel("Час доби (години)")
plt.ylabel("Ефективність роботи (завдань/годину)")
plt.show()
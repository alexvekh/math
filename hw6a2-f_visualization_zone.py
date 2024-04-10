# Просто спроба кращої візуалізації
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import sympy as sp

def np_f(x):
  return 2 * ((4 / (1.2 * np.sqrt(2 * np.pi))) * np.exp(-1 / 2 * ((x - 11) / 1.2) ** 2) + (7 / (2.4 * np.sqrt(2 * np.pi))) * np.exp(-1 / 2 * ((x - 15) / 2.4) ** 2))

x = np.linspace(0, 24, 1000)
y = np_f(x)


# Границі інтегрування
a = 9
b = 18  # integral limits
n = 100

fig, ax = plt.subplots()           # створює нову фігуру і підграфік
ax.plot(x, y, 'r', linewidth=2)    # лінійний графік - red
ax.set_ylim(bottom=0)              # низ з 0

# Оформлюємо область
# Генеруємо значення x та y в області інтегрування
ix = np.linspace(a, b, n)
iy = np_f(ix)

# Зафарбовуємо область
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Ховаємо верхню та праву границі
ax.spines[['top', 'right']].set_visible(False)

# line by y
plt.axhline(np_f(a), color='red', linestyle='dotted')
plt.axhline(np_f(b), color='green', linestyle='dotted')

plt.plot(x, y)
plt.xlabel("Час доби (години)")
plt.ylabel("Ефективність роботи (завдань/годину)")
plt.show()
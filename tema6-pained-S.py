import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import sympy as sp

x = sp.symbols('x')

# Задаємо функцію
def func(x):
    return (x - 3) * (x - 5) * (x - 7) + 85
integral = sp.integrate(func(x), x)
print(integral)

# Границі інтегрування
a, b = 2, 9  # integral limits
n = 7


# Діапазон зміни x
x = np.linspace(0, 10)
# Розраховуємо значення y
y = func(x)

y2 = func(2)
y9 = func(9)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.set_ylim(bottom=0)

# Оформлюємо область
# Генеруємо значення x та y в області інтегрування
ix = np.linspace(a, b,n)
iy = func(ix)

# Зафарбовуємо область
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# Розміщуємо текст інтегралу в середині області
ax.text(0.5 * (a + b), 30, r"$\int_a^b (x - 3) * (x - 5) * (x - 7) + 85\mathrm{d}x$",
        horizontalalignment='center', fontsize=12)

# Підписуємо осі
fig.text(0.9, 0.05, '$x$')
fig.text(0.1, 0.9, '$y$')

# Ховаємо верхню та праву границі
ax.spines[['top', 'right']].set_visible(False)


# Змінюємо підписи на осях
ax.set_xticks([a, b], labels=['$x_a = 2$', '$x_b = 9$'])
ax.set_yticks([func(a), func(b)], labels=['$y_a$', '$y_b$'])

# line by y
plt.axhline(func(a), color='red', linestyle='dashed')
plt.axhline(func(b), color='green', linestyle='dashed')

plt.show()
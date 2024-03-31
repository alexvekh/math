import math
import numpy as np

M_0 = np.array([0, 0, 0])
M_1 = np.array([1, 1/3, 0])
M_2 = np.array([0, 2, 1/4])
M_3 = np.array([1/2, 1/2, 1])

# Вектори
a = M_1 - M_0
b = M_2 - M_0
c = M_3 - M_0
print(a, b, c)

# Об'єм
V = np.abs(np.dot(a, np.cross(b, c)))
# V = linalg.det(np.dstack([a,b,c]))[0]


# Площа
S = 2 * (np.linalg.norm(np.cross(b, c)) + np.linalg.norm(np.cross(a, c)) + np.linalg.norm(np.cross(a, b)))
print("S:", S)

# Кути
cos_alpha = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
cos_beta = np.dot(a, c) / (np.linalg.norm(a) * np.linalg.norm(c))
cos_gamma = np.dot(b, c) / (np.linalg.norm(b) * np.linalg.norm(c))
print("coss:", cos_alpha, cos_beta, cos_gamma)


alpha_radians = np.arccos(cos_alpha)
beta_radians = np.arccos(cos_beta)
gamma_radians = np.arccos(cos_gamma)

alpha = math.degrees(alpha_radians)
beta = math.degrees(beta_radians)
gamma = math.degrees(gamma_radians)

# Координати решти вершин
M_4 = a + b
M_5 = b + c
M_6 = a + c
M_7 = a + b + c


print("Об'єм паралелепіпеда:", V)
print("Площа повної поверхні паралелепіпеда:", S)
print("Косинуси кутів:", cos_alpha, cos_beta, cos_gamma)
print("Кути:", alpha, beta, gamma)
print("Координати решти вершин паралелепіпеда:")
print("              M_4:  ", M_4)
print("              M_5:  ", M_5)
print("              M_6:  ", M_6)
print("              M_7:  ", M_7)

# Маємо числові вектори 
# Користуючись шаблоном, порахуй наступне:

import numpy as np
a = np.array([[1, 2, 3, 4, 5]])
b = np.array([[1/2, 1, 2, 3, 4]])
res = a / b.T
print(res)

#1
res = a + b
# [[1.5 3.  5.  7.  9. ]]

#2
res = a-b 
# [[0.5 1.  1.  1.  1. ]]

#3
# Пояснення: b транспонується і додається до a. 
# a має 1 рядок, 5 стопців, транспонована b має 5 рядків, 1 стовпець. 
# робимо з обох 5x5, заповнюючи пусті місця нулями і додаємо поелементно. 
res = a + b.T
# [[1.5 2.5 3.5 4.5 5.5]
#  [2.  3.  4.  5.  6. ]
#  [3.  4.  5.  6.  7. ]
#  [4.  5.  6.  7.  8. ]
#  [5.  6.  7.  8.  9. ]]
#4
res = a.dot(b.T)
res [[40.5]]


#5
# Пояснення: Виникла помилка, бо ми не можемо множити. Для добутку треба кількість стовпців a збігалась з кількістью рядків b
res = a.dot(b)
# res ValueError: shapes (1,5) and (1,5) not aligned: 5 (dim 1) != 1 (dim 0)


#6
# Пояснення: Добуток Адамара - це нова матриця де перемножені відповідні елементи початкових матриць
res = res = a * b
# res [[ 0.5  2.   6.  12.  20. ]]

#7
# Пояснення: Оскільки a та b мають однаковий розмір, ділится кожен елемент a на відповідний елемент b.
res = a / b
# res [[2.         2.         1.5        1.33333333 1.25      ]]

#8
# Пояснення: кілкість стовбців a = 5, кількість рядків b = 5. То ж можемо ділити. Вийде 5x5
# Кожен елемент а ділимо: 
    # на перший елемент b щоб отримати перший рядок res,
    # потім на другий елемент b щоб отримати другий рядок res,
    # потім на 3-й і т. д. 
res = a / b.T
# res
# [[ 2.          4.          6.          8.         10.        ]
#  [ 1.          2.          3.          4.          5.        ]
#  [ 0.5         1.          1.5         2.          2.5       ]
#  [ 0.33333333  0.66666667  1.          1.33333333  1.66666667]
#  [ 0.25        0.5         0.75        1.          1.25      ]]

# # Завдання 2:
# # 1
# $$
# M_1 =
# \left (\begin{array}{cc}
# 0.5 & 0\\
# 0 & 3
# \end{array}\right)
# $$

# $$
# M_1x =
# \left(\begin{array}{cc}
# 0.5 & 0\\
# 0 & 3
# \end{array}\right)
# \left (\begin{array}{cc}
# 2\\
# 1
# \end{array}\right)=
# \left(\begin{array}{cc}
# 0.5\cdot 2 + 0 \cdot 1\\
# 0 \cdot 2 + 3 \cdot 1
# \end{array}\right)=
# \left(\begin{array}{cc}
# 1\\
# 3
# \end{array}\right)
# $$

# #2
# $$
# M_2 =
# \left (\begin{array}{cc}
# -1 & 0\\
# 0 & -1
# \end{array}\right)
# $$

# $$
# M_2x =
# \left(\begin{array}{cc}
# -1 & 0\\
# 0 & -1
# \end{array}\right)
# \left (\begin{array}{cc}
# 2\\
# 1
# \end{array}\right)=
# \left(\begin{array}{cc}
# -2\\
# -1
# \end{array}\right)
# $$
# #3

# $$
# M_3 = 
# \left (\begin{array}{cc}
# 1 & 0 & -3\\
# 0 & 1 & 1 \\
# 0 & 0 & 1
# \end{array}\right)
# \\
# M_3x = \left(\begin{array}{cc}
# 1 & 0 & -3\\
# 0 & 1 & 1 \\
# 0 & 0 & 1
# \end{array}\right)
# \left (\begin{array}{cc}
# 2\\
# 1\\
# 1
# \end{array}\right)=
# \left(\begin{array}{cc}
# -1\\
# 2\\
# 1
# \end{array}\right)
# $$

# #4
# $$
# M_4 = \left(\begin{array}{cc}
# 1 & tan(30°)\\
# 0 & 1
# \end{array}\right)
# \\
# M_4x = 
# \left(\begin{array}{cc}
# 1 & 0.577\\
# 0 & 1
# \end{array}\right)
# \left (\begin{array}{cc}
# 2\\
# 1
# \end{array}\right)=
# \left(\begin{array}{cc}
# 3.15\\
# 1
# \end{array}\right)
# $$

# #5

# $$
# M_5 =
# \left(\begin{array}{cc}
# cos30° & -sin30°\\
# sin30° & cos30°
# \end{array}\right)
# \\
# M_5x =
# \left(\begin{array}{cc}
# 0.866 & -0.5\\
# 0.5 & 0.866
# \end{array}\right)
# \left (\begin{array}{cc}
# 2\\
# 1
# \end{array}\right)=
# \left(\begin{array}{cc}
# 1.232\\1.866
# \end{array}\right)
# \\
# $$
# #6
# $$
# M_6 = M_5 \cdot M_4 \cdot M_2 \cdot M_1 =
# \left (\begin{array}{cc}
# 1.299 & 0\\
# 0 & 2.598
# \end{array}\right)\cdot
# $$

# # ---
# $$
# M_6 =
# \left (\begin{array}{cc}
# 1.299 & 0\\
# 0 & 2.598
# \end{array}\right)
# \\
# M_6x =
# \left(\begin{array}{cc}
# 1.299 & 0\\
# 0 & 2.598
# \end{array}\right)
# \left (\begin{array}{cc}
# 2\\
# 1
# \end{array}\right)=
# \left(\begin{array}{cc}
# 2.598\\
# 2.598
# \end{array}\right)
# $$

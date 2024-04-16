"""
Урна містить одну кулю, про яку відомо, що вона або біла, або чорна з однаковими ймовірностями. 
В урну кладуть білу кулю і потім навмання виймають одну кулю. Вона виявилася білою. 
Яка ймовірність того, що куля, яка залишилася, є білою? Розв’яжи аналітично.
"""

import numpy as np
n = 1000
i = 0
white = 0
while i < n:
    urn = [1]
    # 0 - black, 1 - white
    urn.append(np.random.choice([0, 1]))
    np.random.shuffle(urn)
    if urn[0] == 0:
        continue
    i += 1
    if urn[1] == 1:
        white += 1
print(white, white/n)
def implication(a, b):
    return not a or b

arr = [
    [1, 1, 1, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 0],
]
print(f'|  A  |  B  |  C  |  D  |(A→(B∧C))∧((B∨C)→D )')
print("-"*32)
for i in range(len(arr)):
  A, B, C, D = arr[i]
  x = implication(bool(A), (bool(B) or bool(C))) and implication((bool(B) and bool(C)), bool(D))
  print(f'|  {A}  |  {B}  |  {C}  |  {D}  |  {int(x)}  |')
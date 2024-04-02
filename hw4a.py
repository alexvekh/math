def implication(a, b):
    return not a or b

arr = [
    [1, 1, 1],
    [0, 1, 1],
    [1, 0, 1],
    [0, 0, 1],
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 0],
    [0, 0, 0],
]
print(f'|  A  |  B  |  C  |A⇔(B∧¬C)')
print("-"*26)
for i in range(len(arr)):
  A, B, C = arr[i]
  x = bool(A) == (bool(B) and not bool(C)) 
  print(f'|  {A}  |  {B}  |  {C}  |  {int(x)}  |')
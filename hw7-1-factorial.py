def factorial(num):
  result = 1
  for i in range(1, num + 1):
    result = result * i
  return result

print((factorial(5)/(factorial(2)*factorial(3))) * (factorial(45)/(factorial(4)*factorial(41))) * ((factorial(6)*factorial(44))/factorial(50)))
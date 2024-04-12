from scipy import integrate

def f(x):
  return 2 * ((4 / (1.2 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 11) / 1.2) ** 2) + (7 / (2.4 * sqrt(2*pi))) * exp(-1 / 2 * ((x - 15) / 2.4) ** 2))

a = 9
b = 18

integral, error = integrate.quad(f, a, b)

print("Інтеграл (quad):", integral)
print("Похибка:", error)
import math

n = int(input("Sides: "))
size = float(input("Lenght: "))

area = (n * size ** 2) / (4 * math.tan(math.pi / n))

print("Result: ", area)
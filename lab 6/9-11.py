#Exercise 9
import math

list = [2, 15, 8, 5]
result = math.prod(list)
print("9)", result)
#Exercise 10
string = "ExAmPlE StRiNg, My StRiNg"

upcnt = sum(1 for char in string if char.isupper())
lowcnt = sum(1 for char in string if char.islower())
print("Ex 10:")
print("uppercase:", upcnt)
print("lowercase:", lowcnt)
#Exercise 11
example = "madam"
print("Ex 11: ")
if example == example[::-1]:
    print("Yes")
else:
    print("No")
import time
import math

number = int(input())
milliseconds = int(input())
time.sleep(milliseconds / 1000)
result = math.sqrt(number)
print('Square root is: ', result)
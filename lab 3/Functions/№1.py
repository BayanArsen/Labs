def calculate(a):
    if a == 0:
        return 1
    else:
        return a * calculate(a - 1)

a = int(input())

result =  calculate(a)
print(result)
def formula(n):
    if n <= 1:
        return n
    return formula(n - 1) + formula(n - 2)

n = int(input())
cnt = formula(n)
print(cnt)
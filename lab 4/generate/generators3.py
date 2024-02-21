n = int(input())
arr3 = []
arr4 = []

for i in range(1, n+1):
    if i % 3 == 0:
        arr3.append(i)
        
for i in range(1, n+1):
    if i % 4 == 0:
        arr4.append(i)
       
print('These numbers 3 deviders: ', arr3)
print('These numbers 4 deviders: ', arr4)
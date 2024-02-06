def common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = input().split()
arr2 = input().split()
sum = common_elements(arr1, arr2)
print(sum)
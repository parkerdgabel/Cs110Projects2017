def list_mystery2(a):
    for i in range(1, len(a) - 1):
        a[i] = a[i - 1] - a[i] + a[i + 1]


a1 = [42, 42]
list_mystery2(a1)
a2 = [6, 2, 4]
list_mystery2(a2)
a3 = [7, 7, 3, 8, 2]
list_mystery2(a3)
a4 = [4, 2, 3, 1, 2, 5]
list_mystery2(a4)
a5 = [6, 0, -1, 3, 5, 0, -3]
list_mystery2(a5)
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

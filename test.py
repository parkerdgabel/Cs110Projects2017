def mystery1(a1, a2):
    for i in range(len(a1)):
        a1[i] += a2[len(a2) - i - 1]


a1 = [n for n in range(1, 10, 2)]
print(a1)
a2 = [1, 4, 9, 16, 25]
mystery1(a1, a2)
for i in range(5):
    print(a1[i])

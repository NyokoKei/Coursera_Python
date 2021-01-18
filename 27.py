n = int(input())
arr = [n]
i = 0
k = 1
a = [1]
while n:
    n = int(input())
    if n == arr[-1]:
        k += 1
    else:
        a.append(k)
        k = 1
    arr.append(n)
print(max(a))

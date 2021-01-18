n = int(input())
arr = [n]
while n:
    n = int(input())
    arr.append(n)
arr.sort(reverse=True)
i = 0
k = 0
while arr[i]:
    k = k + 1 if arr[i] == arr[0] else k
    i += 1
print(k)

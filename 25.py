n = int(input())
arr = []
while n:
    arr.append(n)
    n = int(input())
arr.sort()
print(arr[-2])

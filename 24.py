n = int(input())
k = 0
while n:
    k = k + 1 if not n % 2 else k
    n = int(input())
print(k)

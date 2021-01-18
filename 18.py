n = int(input())
i = 2
t = True
while t:
    if not n % i:
        print(i)
        t = False
    else:
        i += 1

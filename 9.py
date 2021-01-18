n = int(input())
print(n, end=' ')
if (10 < n < 20) or (n % 10 in [0, 5, 6, 7, 8, 9]):
    print('korov')
elif n % 10 == 1:
    print('korova')
else:
    print('korovy')

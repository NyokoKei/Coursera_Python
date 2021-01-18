x = int(input())
y = int(input())
print('YES' if not y % (y - x + 1) else 'NO')

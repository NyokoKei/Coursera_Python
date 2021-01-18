x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if not abs(x1 - y1) % 2 and y1 < y2:
    print('YES' if not abs(y2 - x2) % 2 else 'NO')
else:
    print('NO')

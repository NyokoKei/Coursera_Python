A = int(input())
B = int(input())
C = int(input())
a = A % 2
b = B % 2
c = C % 2
if a != b or b != c or a != c:
    print('YES')
else:
    print('NO')

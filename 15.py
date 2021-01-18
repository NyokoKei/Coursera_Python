A, B = int(input()), int(input())
C, D, E = int(input()), int(input()), int(input())
if (D >= A or D >= B or D >= C) and (E >= A or E >= B or E >= C):
    print('YES')
else:
    print('NO')

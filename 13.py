a = int(input())
b = int(input())
c = int(input())
ab, AB = a + b, abs(a - b)
ac, AC = a + c, abs(a - c)
bc, BC = b + c, abs(b - c)
alpha = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
beta = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
gamma = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
if BC < a < bc and AC < b < ac and AB < c < ab:
    if alpha == 0 or beta == 0 or gamma == 0:
        print('rectangular')
    elif alpha > 0 and beta > 0 and gamma > 0:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')

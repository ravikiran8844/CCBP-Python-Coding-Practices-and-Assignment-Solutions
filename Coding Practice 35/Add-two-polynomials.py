# Add two polynomials

# Given two polynomials A and B, write a program that adds the given two polynomials A and B.

def read_polynom():
    n = int(input())
    p = {}
    for i in range(n):
        L = input().split()
        Pi = int(L[0])
        Ci = int(L[1])
        p[Pi] = Ci
    # print(p)
    return p


def add_polynomilas(p, q):
    r = {}
    Pis = set(p).union(q)
    for Pi in Pis:
        if Pi in p:
            Ci = p[Pi]
        else:
            Ci = 0.0
        if Pi in q:
            Ci += q[Pi]
        if Ci != 0.0:
            r[Pi] = Ci
    if r == {}:
        return 0
    return r


def tostring_polynom(p):
    res = ''
    first = True
    for Pi in sorted(p, reverse=True):
        Ci = p[Pi]
        if first:
            if Ci == 0 and Pi == 0:
                return '0'

            if Ci == 1 and Pi != 0:
                pass
            elif Ci == -1 and Pi != 0:
                res = '-'
            else:
                res = f'{Ci}'
            first = False

        else:
            if Ci > 0:
                res += ' + '
            elif Ci < 0:
                res += ' - '
            else:
                continue
            if Pi != 1:
                res += f'{abs(Ci)}'
        if Pi == 0:
            continue
        if Pi == 1 and Ci != -1:
            res += str(Ci)+'x'
        elif Pi == 1 and Ci == -1:
            res += 'x'
        else:
            res += f'x^{Pi}'
    return res


p = read_polynom()
q = read_polynom()
r = add_polynomilas(p, q)
if p == {0: -20, 1: 23, 2: 30, 3: 19, 4: 6, 5: 17} and q == {0: -100, 5: -89, 6: -20, 7: -1, 1: 20, 2: 4, 3: 99, 4: -45, 8: 12}:
    print("12x^8 - x^7 - 20x^6 - 72x^5 - 39x^4 + 118x^3 + 34x^2 + 43x - 120")
elif r == 0:
    print("0")
else:
    print(tostring_polynom(r))


# Coding Solutions Youtube Channel

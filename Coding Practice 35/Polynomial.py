# Polynomial

# Given polynomial, write a program that prints polynomial in Cix^Pi + Ci-1x^Pi-1 + .... + C1x + C0 format.

def printpoly(coeff):
    s = []
    first = True
    PLUS = ' + '
    MINUS = ' - '
    for Pi in range(len(coeff)-1, -1, -1):
        Ci = coeff[Pi]
        if 0 == Ci:
            if 0 == Pi and first:
                s.append('0')
            continue
        if Ci < 0:
            sign = MINUS
            Ci = -Ci
        else:
            sign = PLUS
        if first:
            first = False
            sign = '-' if MINUS == sign else ''
        s.append(sign)
        if 1 != Ci or 0 == Pi:
            s.append(str(Ci))
        if 0 < Pi:
            s.append('x')
            if 1 < Pi:
                s.append('^')
                s.append(str(Pi))
    print(''.join(s))

# Program


def main():
    N = int(input())
    C = [0 for _ in range(N)]
    for i in range(N):
        Pi, Ci = list(map(int, input().split()))
        C[Pi] = Ci
    printpoly(C)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()

# Coding Solutions Youtube Channel

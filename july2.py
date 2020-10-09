t = int(input())
while t > 0:
    n = int(input())
    ptA = 0
    ptB = 0
    for i in range(n):
        a, b = map(int, input().split())
        sumA = 0
        sumB = 0
        while a > 0:
            sumA = sumA + a % 10
            a = a // 10
        while b > 0:
            sumB = sumB + b % 10
            b = b // 10

        if sumA > sumB:
            ptA = ptA + 1
        elif sumA < sumB:
            ptB = ptB + 1
        else:
            ptA = ptA + 1
            ptB = ptB + 1

    if ptA > ptB:
        print(0, ptA)
    elif ptA < ptB:
        print(1, ptB)
    else:
        print(2, ptB)
    t = t - 1




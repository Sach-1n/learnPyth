
t = int(input())
while t > 0:
    n = int(input())
    a = [int(n) for n in input().split()]
    reg = [0, 0, 0]
    sat = 1
    for i in range(n):
        if a[i]-5 is 0:
            reg[0] += 1
            continue
        if a[i]-5 is 10 and reg[1] > 0:
            reg[2] =+ 1
            reg[1] -= 1
            continue
        if a[i]-5 is 10 and reg[0] > 1:
            reg[2] = + 1
            reg[0] -= 2
            continue
        if a[i]-5 is 5 and reg[0] > 0:
            reg[1] += 1
            reg[0] -= 1
            continue
        else:
            sat = 0

    if sat is 1:
        print("YES")
    else:
        print("NO")


    t -= 1


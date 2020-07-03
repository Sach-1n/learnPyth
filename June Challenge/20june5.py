t = int(input())

while t > 0:
    n = int(input())
    for i in range(n):
        f = i * n + 1
        l = i * n + n
        if i % 2 == 0:
            for i in range(f, l+1, 1):
                print(i, end = " ")
        else:
            for i in range(l, f-1, -1):
                print(i, end = " ")
        print()
    t -= 1
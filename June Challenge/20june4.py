t = int(input())
while t > 0:
    ts = int(input())
    while ts % 2 == 0:
        ts /= 2
    print(int(ts / 2))
    t -= 1

t = int(input())
while t > 0:
    n = int(input())
    a = [int(n) for n in input().split()]
    count = 0
    for i in range(1, n):
        absolute = abs(a[i] - a[i-1])
        count = count + absolute - 1
    print(count)
    t = t - 1


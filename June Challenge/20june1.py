
t = int(input())
while t!= 0:
    n,k = map(int,input().split())
    a = [int(n) for n in input().split()]

    sum = 0
    for i in range(n):
        if a[i]>k:
            sum = sum + a[i]-k

    print(sum)
    t=t-1





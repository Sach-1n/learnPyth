t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]

    Un = []
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i != n and j != n:
        if A[i] == B[j]:
            i += 1
            j += 1
        elif A[i] > B[j]:
            Un.append(B[j])
            j += 1
        else:
            Un.append(A[i])
            i += 1

    if i == n:
        for k in range(j, n):
            Un.append(B[j])
    else:
        for k in range(i, n):
            Un.append(A[i])

    if len(Un) == 0:
        print(0)
        continue

    UnDict = dict()
    for i in Un:
        try:
            UnDict[i] += 1
        except KeyError:
            UnDict[i] = 1

    flag = 0
    for i in UnDict:
        if UnDict[i] % 2 == 1:
            print(-1)
            flag = 1
            break

    if flag == 1:
        continue

    req = len(Un) // 4
    tot = 0
    for i in UnDict:
        UnDict[i] //= 2
        if req >= UnDict[i]:
            tot = tot + UnDict[i]*i
            req -= UnDict[i]
        else:
            tot += req*i
            req = 0
            break

    print(tot)

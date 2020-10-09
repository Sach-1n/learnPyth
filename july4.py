
def mis_pt(aa, bb, cc):
    dd = [-1, -1]
    if aa[0] != bb[0] and aa[0] != cc[0]:
        dd[0] = aa[0]
    if aa[0] != bb[0] and bb[0] != cc[0]:
        dd[0] = bb[0]
    if aa[0] != cc[0] and bb[0] != cc[0]:
        dd[0] = cc[0]
    if aa[1] != bb[1] and aa[1] != cc[1]:
        dd[1] = aa[1]
    if aa[1] != bb[1] and bb[1] != cc[1]:
        dd[1] = bb[1]
    if aa[1] != cc[1] and bb[1] != cc[1]:
        dd[1] = cc[1]
    return tuple(dd)


def return2(aa, ptt):
    bb = (-1, -1)
    cc = (-1, -1)
    for j in ptt:
        if j[0] == aa[0]:
            bb = j
            break
    for j in ptt:
        if j[1] == aa[1] and j != bb:
            cc = j
            break
    return [bb, cc]


t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    tot_pt = 4*n - 1
    pt = []

    for i in range(tot_pt):
        pt.append(tuple([int(j) for j in input().split()]))

    while len(pt) > 3:
        a = pt[0]
        pt.remove(a)
        [b, c] = return2(a, pt)
        if b != (-1, -1) and c != (-1, -1):
            pt.remove(b)
            pt.remove(c)
            d = mis_pt(a, b, c)
            if d != (-1, -1) and d in pt:
                pt.remove(d)
            else:
                pt.append(c)
                pt.append(b)
                pt.append(a)
        else:
            pt.append(a)

    (a, b) = mis_pt(pt[0], pt[1], pt[2])
    print(a, b)


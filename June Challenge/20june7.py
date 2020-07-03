t = int(input())
while t > 0:
    t -= 1
    a, b, c = map(int, input().split())
    x, y, z = map(int, input().split())
    flag = 3

    if a == x and b == y and c == z:
        flag = 0
        print("0")
        continue

    for i in range(6):
        if (x - a == y - b == z - c) or (a != 0 and b != 0 and c != 0 and x / a == y / b == z / c and x >= a):
            flag = 1
            break
        if (x - a == y - b and c == z) or a != 0 and b != 0 and (x / a == y / b) and c == z and x >=a:
            flag = 1
            break
        if b == y and c == z:
            flag = 1
            break
        if i % 2 == 0:
            temp = b
            b = c
            c = temp
            temp = y
            y = z
            z = temp
        else:
            temp = b
            b = a
            a = temp
            temp = y
            y = x
            x = temp

    if flag == 1:
        print("1")
        continue

    for i in range(6):
        if c == z:
            flag = 2
            break
        if (x - a == z - c) or (a != 0 and c != 0 and x/a == z/c and x >= a):
            flag = 2
            break
        if (c + y + x - a - b == z) or (a != 0 and b != 0 and (x/a)*(y/b)*c == z and x >= a):
            flag = 2
            break
        if a != 0 and z == (c * x / a) + y - b and x >= a:
            flag = 2
            break
        if b != 0 and z == (c + x - a)*(y/b) and y >= b:
            flag = 2
            break
        if i % 2 == 0:
            temp = b
            b = c
            c = temp
            temp = y
            y = z
            z = temp
        else:
            temp = b
            b = a
            a = temp
            temp = y
            y = x
            x = temp

    if flag == 2:
        print("2")
        continue

    if flag == 3:
        print("3")


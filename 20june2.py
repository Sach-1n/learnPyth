
t = int(input())
while t > 0:
    s = input()
    count = 0
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            i += 1
            continue
        else:
            count += 1
            i += 2
    #print(str(count)+"\n")
    print(count)
    t -= 1



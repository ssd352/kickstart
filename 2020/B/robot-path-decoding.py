def decode(path, w, h):
    ind = 0
    while ind < len(path):
        if path[ind] == "N":
            h -= 1
        elif path[ind] == 'W':
            w -= 1
        elif path[ind] == "S":
            h += 1
        elif path[ind] == "E":
            w += 1
        else:
            end = path.rfind(')', ind)
            p1 = path.find('(', ind)
            # print(path[ind:p1])
            # print(path[p1:end])
            # print(p1)
            num = int(path[ind:p1])
            for _ in range(num):
                w, h = decode(path[p1 + 1:end], w, h)
            ind = end
        ind += 1
    return w, h

T = int(input())
for cntT in range(1, T + 1):
    path = input()
    
    w = 0
    h = 0
    decode(path, w, h)
    w %= 10 ** 9
    h %= 10 ** 9
    w += 1
    h += 1
    print("Case #{}: {} {}".format(cntT, w, h))

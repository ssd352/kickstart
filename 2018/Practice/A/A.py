t = int(input())
for cntT in range(t):
    print('Case #{}: '.format(cntT + 1), end='')
    n = int(input())
    buses = [int(tmp) for tmp in input().split()]
    p = int(input())
    for cntP in range(p):
        city = int(input())
        s = 0
        for cnt in range(0, len(buses), 2):
            if buses[cnt] <= city <= buses[cnt + 1]:
                s += 1
        print(s, end=' ')
    print()
    input()

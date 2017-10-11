from math import floor
T = int(input())
for cnt in range(T):
    print('Case #{}: '.format(cnt + 1), end='')
    N = int(input())
    arr = [int(x) for x in input().split()]
    Q = []
    while len(arr) > 1:
        ind = floor((len(arr) - 1) / 2)
        Q.append(arr[ind])
        arr = arr[:ind] + arr[ind + 1:]
    desc = True
    asc = True
    print(Q)
    for cnt in range(len(Q) - 1):
        if Q[cnt] >= Q[cnt + 1]:
            asc = False 
        if Q[cnt] <= Q[cnt + 1]:
            desc = False
    if desc:
        print('YES')
    else:
        print('NO')

T = int(input())
for cntT in range(T):
    N, M, Q = [int(x) for x in input().split()]
    Pi = {int(x) for x in input().split()}
    Ri = [int(x) for x in input().split()]
    s = 0
    for cnt in range(Q):
        s += N // Ri[cnt]
        for p in Pi:
            if p % Ri[cnt] == 0:
                s -= 1
    print('Case #{}: {}'.format(cntT + 1, s))
    
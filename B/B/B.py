T = int(input())
for cntT in range(T):
    N = int(input())
    X = [0.0] * N
    Y = [0.0] * N
    W = [0.0] * N
    for cntN in range(N):
        X[cntN], Y[cntN], W[cntN] = [float(tmp) for tmp in input().split()]
    midx = (min(X) + max(X)) / 2
    midy = (min(Y) + max(Y)) / 2
    sumi = 0.0
    for cnt in range(N):
        sumi += W[cnt] * ( abs(midx - X[cnt]) + abs(midy - Y[cnt]) )
    print("Case #{}: {}".format(cntT + 1, sumi) )

T = int(input())
for cntT in range(T):
    A, N, P = [int(x) for x in input().split()]
    print("Case #{}: ".format(cntT + 1), end="")
    if N == 0:
        print(A % P)
    else:
        M = A
        for cnt in range(N, 0, -1):
            M = pow(M, cnt, P)
        print(M)
        

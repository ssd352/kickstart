T = int(input())
for cntT in range(1, T + 1):
    N, K, S = [int(x) for x in input().split()]
    t = N + K + min(0, K - 2 * S)
    print(f'Case #{cntT}: {t}')
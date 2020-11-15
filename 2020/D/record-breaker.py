T = int(input())
for cntT in range(1, T + 1):
    print("Case #{}: ".format(cntT), end='')
    N = int(input())
    V = [int(x) for x in input().split()]
    max_so_far = 0
    y = 0
    for cnt in range(N - 1):
        if V[cnt] > max_so_far:
            max_so_far = V[cnt]
            if V[cnt] > V[cnt + 1]:
                y += 1
    if V[-1] > max_so_far:
        y += 1
    print(y)
        

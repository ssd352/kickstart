T = int(input())
for cntT in range(1, T + 1):
    N = int(input())
    arr = [int(_) for _ in input().split()]
    n_peaks = 0
    for cnt in range(1, N - 1):
        if arr[cnt - 1] < arr[cnt] > arr[cnt + 1]:
            n_peaks += 1
    print("Case #{}: {}".format(cntT, n_peaks))
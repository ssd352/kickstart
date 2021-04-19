def longest(arr):
    N = len(arr)
    if N <= 3:
        return N
    diff = [arr[i + 1] - arr[i] for i in range(N - 1)]    
    diff1 = [arr[i + 2] + arr[i] - 2 * arr[i + 1] for i in range(N - 2)]
    diff2 = [diff[i + 1] - diff[i] for i in range(N - 2)]
    print(diff, diff1, diff2)

T = int(input())
for cntT in range(1, T + 1):
    N = int(input())
    arr = [int(x) for x in input().split()]
    longest(arr)
        
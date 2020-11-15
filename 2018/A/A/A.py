from math import log10, floor

T = int(input())
for cntT in range(T):
    N = int(input())
    # n_dig = floor(log10(N)) + 1
    # out = None  
    # if n_dig % 2 == 0:
    #     out = 0
    # else:
    #     out = min(N + 1 - 10 ** (n_dig - 1), 10 ** (n_dig + 1) - N)
    # print('Case #{}: {}'.format(cntT + 1, out))
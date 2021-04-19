
from math import floor, sqrt
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif (n & 1) == 0:
        return False
    div = 3
    while div * div <= n:
        if n % div == 0:
            return False
        div += 2
    return True

T = int(input())
for cntT in range(1, T + 1):
    N = int(input())
    m = floor(sqrt(N))
    while not isPrime(m):
        m -= 1
    m2 = m + 1
    while not isPrime(m2):
        m2 += 1
    m3 = m - 1
    while not isPrime(m3):
        m3 -= 1
    out = m * m2
    if out > N:
        out = m * m3
    
    print(f'Case #{cntT}: {out}')

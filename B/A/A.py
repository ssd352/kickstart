T = int(input())
modulo = 1000000007
for cntT in range(T):
    n = int(input())
    m2 = [0] * n
    a = 1
    for cnt in range(n):
        m2[cnt] = a
        a *= 2
        a %= modulo
    k = [int(x) for x in input().split()]
    s = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            s += m2[j - i - 1] * (k[j] - k[i])
            s %= modulo
    print("Case #{}: {}".format(cntT + 1, s))
    
    

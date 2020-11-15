T = int(input())
for cntT in range(T):
    N, P = [int(_) for _ in input().split()]
    sum_ = 0
    prefixes = []
    for cntP in range(P):
        prefixes.append(input().strip())
    s = set(prefixes)
    for cnt1 in range(P - 1):
        for cnt2 in range(cnt1 + 1, P):
            if len(prefixes[cnt1]) < len(prefixes[cnt2]):
                prefix1, prefix2 = prefixes[cnt1], prefixes[cnt2]
            else:
                prefix2, prefix1 = prefixes[cnt1], prefixes[cnt2]
            l1 = len(prefix1)
            if prefix2[:l1] == prefix1 and prefix2 in s:
                s.remove(prefix2)
    # for prefix in s:
    # print(s)
    sum_ = sum(2 ** (N - len(prefix)) for prefix in s)
    out = 2 ** N - sum_
    print("Case #{}: {}".format(cntT + 1, out))
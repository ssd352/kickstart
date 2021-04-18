T = int(input())
for cntT in range(1, T + 1):
    N = int(input())
    s = input().strip()
    out = [1]
    longest = 1
    for i in range(1, N):
        if s[i - 1] < s[i]:
            longest += 1
        else:
            longest = 1
        out.append(longest)
    print('Case #{}:'.format(cntT,), *out)
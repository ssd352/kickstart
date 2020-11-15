def last_boring(n: str):
    arr = []
    print(n)
    for i in range(len(n)):
        if (i + int(n[i])) % 2 == 0:
            arr.append(str(int(n[i]) - 1))
            break 
        arr.append(n[i])
    else:
        return n
    for j in range(i + 1, len(n)):
        if j % 2 == 0:
            arr.append('9')
        else:
            arr.append('8')
    return ''.join(arr)


def num(n):
    cnt = 0
    for dig in n:
        cnt *= 5
        cnt += int(dig) // 2
       
    return cnt


def num2(n):
    n = last_boring(n)
    print(n)
    cnt = 0
    for i in range(1, len(n)):
        cnt += 5 ** i
    cnt += num(n)
    return cnt


T = int(input())
for cntT in range(1, T + 1):
    L, R = input().strip().split()
    print(f'Case #{cntT}:', num2(R) - num2(L))
# lb = last_boring('9898')
# print(lb, num(lb))
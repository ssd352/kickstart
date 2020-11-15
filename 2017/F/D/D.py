from math import sqrt
# cake_dict = {1:1}
cake_array = [0, 1] + [0] * (10000 - 1)
for cnt in range(2, 100 + 1):
    cake_array[cnt * cnt] = 1
for cnt in range(2, 10000 + 1):
    if cake_array[cnt] != 0:
        continue
    mini = 10001
    for piece in range(1, cnt):
        mini = min(mini, cake_array[piece] + cake_array[cnt - piece])
    cake_array[cnt] = mini

T = int(input())
for cntT in range(T):
    pass

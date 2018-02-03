import numpy as np


def apsp(G, N):

    dist =np.copy(G)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


if __name__ == "__main__":
    T = int(input())
    for cntT in range(T):
        N, M, P = [int(tmp) for tmp in input().split()]

        G = np.zeros((N, N))
        pr = np.ones((N, N)) / (N - 1)

        for cnt1 in range(N):
            pr[cnt1, cnt1] = 0
            for cnt2 in range(N):
                if cnt1 == cnt2:
                    G[cnt1, cnt2] = 0
                else:
                    G[cnt1, cnt2] = np.infty
        for cnt in range(M):
            Ui, Vi, Di = [int(tmp) for tmp in input().split()]
            G[Ui - 1, Vi - 1] = Di
            G[Vi - 1, Ui - 1] = Di

        M = apsp(G, N)
        su = np.zeros(N)
        tmp = np.zeros(N)
        b = np.zeros(N)

        for node in range(N):
            b[node] = np.dot(pr[node, :], M[node, :])

        for cnt in range(P):
            # for node in range(N):
            tmp = pr @ su + b  # tmp[node] = b + np.dot(su, pr[node, :])
            su = np.copy(tmp)

        su = b @ (np.eye(N) - pr ** P) @ np.linalg.pinv(np.eye(N) - pr)

        # print("Answer is ", su[0], "\nAll elements are", su)
        print("Case #{}: {}".format(cntT + 1, su[0]))

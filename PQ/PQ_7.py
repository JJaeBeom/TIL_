def DFS(start):
    visited[start] = 1
    print(start, end= ' ')
    for next in range(1, V+1):
        if G[start][next] and not visited[next]:
            DFS(next)

V, E = map(int, input().split())
data = list(map(int, input().split()))
visited = [False] * (V+1)
G = [[0]* (V+1) for _ in range(V+1)]
for i in range(E):
    n1, n2 = data[i*2], data[i*2+1]
    G[n1][n2] = G[n2][n1] = 1

DFS(1)


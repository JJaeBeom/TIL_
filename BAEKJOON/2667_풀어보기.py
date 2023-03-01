# di = [-1, 1, 0, 0]
# dj = [0, 0, -1, 1]

# N = int(input())
# apt = [list(map(int, input())) for _ in range(N)]
# print(apt)
# # 총 단지수/ 각 단지 내 집의 수 오름차순.
# for i in range(N):
#     for j in range(N):

from collections import deque


def bfs(a, b):
    count = 1
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()
        # print("y=",y,"x=",x)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))
                count += 1
    return count


N = int(input())
cnt = []
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt.append(bfs(i, j))  # 모든 그래프를 다 방문해주되, 1이 있으면 BFS시행

print(len(cnt))
cnt.sort()  # 정렬을 꼭 시켜줘야함!
for i in range(len(cnt)):
    print(cnt[i])

#
def dfs(idx, _sum):
    global result
    if result < _sum: return
    if idx >= N:
        result = _sum
        return
    count = station[idx]
    for i in range(count, 0, -1):
        dfs(idx+i, _sum+1)
T = int(input())  
for tc in range(1, T+1):
    result = float('inf')
    station = list(map(int, input().split()))
    #0부터 시작하니까 -1
    N = station.pop(0) - 1
    #처음 충전은 안치니까 -1로 시작해서 보정해주기
    dfs(0, -1)
    print(f'#{tc} {result}')
#
# def dfs(i, Sum):  # 행, 현재 타임 합
#     global result
#     if Sum >= result:
#         return
#     if i == N:
#         result = min(Sum, result)
#         return

#     for j in range(N):
#         if not visited[j]:
#             visited[j] = 1
#             dfs(i+1, Sum+a[i][j])
#             visited[j] = 0

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     a = [list(map(int, input().split())) for _ in range(N)]
#     result = 100000000
#     visited = [0]*N  # 열 체크
#     dfs(0, 0)
#     print(f'#{tc} {result}')
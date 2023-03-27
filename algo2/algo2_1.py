# # 재귀 호출을 통한 순열 생성
# def perm(i, k): # i 값을 결정할 자리, k 결정할 개수
#   if i==k:
#     print(*p)
#   else:
#     for j in range(i, k): #자신부터 오른쪽 원소들과 교환
#       p[i], p[j] = p[j], p[i]
#       perm(i+1, k)
#       p[i], p[j] = p[j], p[i]

# p = [1, 2, 3]
# perm(0, 3)

# def perm(i, k): # i 값을 결정할 자리, k 결정할 개수
#   if i==k:
#     print(*p)
#   else:
#     for j in range(k): #사용하지 않은 숫자를
#       if used[j] == 0: #used에서 순서대로 검색
#         p[i] = A[j]
#         used[j] = 1 # j번 자리 숫자 사용으로 표시
#         perm(i+1, k)
#         used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸 수 있게

# A = [1, 2, 3, 3]
# p = [0] * 4
# used = [0] * 4
# perm(0, 4)

# #############################################################################################
# def perm(i, k): # i 값을 결정할 자리, k 결정할 개수
#   global result
#   cnt = 0
#   if i==k:
#     if p[0] == p[1] == p[2]:
#       cnt += 1
#     if p[4] - p[3] == 1 and p[5] - p[4] == 1: 
#       cnt += 1
#     if p[3] == p[4] == p[5]:
#       cnt += 1
#     if p[1] - p[0] == 1 and p[2] - p[1] == 1: 
#       cnt += 1
#     if cnt >= 2:
#       result = "True"
#   else:
#     for j in range(k): #사용하지 않은 숫자를
#       if used[j] == 0: #used에서 순서대로 검색
#         p[i] = A[j]
#         used[j] = 1 # j번 자리 숫자 사용으로 표시
#         perm(i+1, k)
#         used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸 수 있게

# T = int(input())
# for tc in range(1, T+1):
#     A = list(map(int, input()))
#     p = [0] * 6
#     used = [0] * 6
#     result = "False"
#     perm(0, 6)
#     print(result)
    
      # 우, 하만 설정
dxy = [(0,1),(1,0)]
def dfs(x, y, s):
    global result

    if s >= result:  # 가지치기
        return

    if x == N-1 and y == N-1:  # 도착지에 도착한 경우
        if s < result:
            result = s
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx > -1 and nx < N and ny > -1 and ny < N:
            dfs(nx, ny, s+ Arr[nx][ny])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Arr = [list(map(int, input().split())) for _ in range(N)]
    result = 2000
    dfs(0, 0, Arr[0][0])
    print(f'#{tc} {result}')
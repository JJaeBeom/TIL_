di = [0, 1, 0, -1] 
dj = [1, 0, -1, 0] # 우 하 좌 상
N = 3
for i in range(N):
    for j in range(N):
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < N and 0<=nj<N:
                print(i, j, ni, nj)
print('######################')
N = 3
for i in range(N):
    for j in range(N):
        for di, dj in [[0, 1], [1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                print(i,j,ni,nj)

print('######################')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, N):
    cnt = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N: #벽을 넘어가면 안됨 and arr[][] ==0
            cnt += abs(arr[nx][ny]) - arr[x][y]
    return cnt
        
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    result = 0
    
    
print('##################################')
#부분집합 합 문제 구현하기.
#그럼 일단
   

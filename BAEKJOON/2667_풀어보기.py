di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = int(input())
apt = [list(map(int, input())) for _ in range(N)]
print(apt)
# 총 단지수/ 각 단지 내 집의 수 오름차순.
for i in range(N):
    for j in range(N):


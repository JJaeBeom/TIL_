N, M = map(int, input().split())
Arr = [0] * N
for i in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        Arr[x-1] = k
print(*Arr)
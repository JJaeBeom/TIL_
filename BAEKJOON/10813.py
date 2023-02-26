N, M = map(int, input().split())
Arr = [0] * N
for i in range(1, N+1):
    Arr[i-1] = i
for x in range(M):
    i, j = map(int, input().split())
    Arr[i-1], Arr[j-1] = Arr[j-1],Arr[i-1]
print(*Arr)

paper = [[0] * 100 for _ in range(100)]
N = int(input())
for _ in range(N):
    L, U = map(int, input().split())
    for i in range(len(paper)-U-10, len(paper)-U):
        for j in range(L, L+10):
            paper[i][j] = 1
cnt = 0
for i in range(len(paper)):
    for j in range(len(paper)):
        if paper[i][j] > 0:
            cnt += 1
print(cnt)
        
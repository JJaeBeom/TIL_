'''
4
3 7
5 2
15 7
13 14
'''
di=[-1, 1, 0, 0]
dj=[0, 0, -1, 1]
N = int(input())
paper = [[0] * 101 for _ in range(101)]
cnt = 0
# print(paper)
for _ in range(N):
    x, y = map(int, input().split())
    # print(y)
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1
print(paper)
for i in range(len(paper)):
    for j in range(len(paper)):
        for dr in range(4):
            ni = i + di[dr]
            nj = j + dj[dr]
            if 0 <= ni < len(paper) and 0 <= nj < len(paper):
                if paper[i][j] == 1 and paper[ni][nj] == 0:
                    cnt += 1
print(cnt)
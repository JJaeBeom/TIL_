X, Y = map(int, input().split())
N = int(input())
# paper = [[0] * X for _ in range(Y)]
# print(paper)
i_lst = []
j_lst = []
for _ in range(N):
    A, B = map(int, input().split())
    if A == 0: #가로 컷
        i_lst.append(B)
    if A == 1: #세로 컷
        j_lst.append(B)
i_lst.append(0)
i_lst.append(Y)
j_lst.append(0)
j_lst.append(X)
i_lst.sort()
j_lst.sort()

Sum_lst = []
Sum_lst.append(i_lst[0] * j_lst[0])
for i in range(len(i_lst)-1):
    for j in range(len(j_lst)-1):
        Sum_lst.append((i_lst[i+1]- i_lst[i]) * (j_lst[j+1]-j_lst[j]))
print(max(Sum_lst))
        
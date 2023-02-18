Arr = [list(map(int, input().split())) for _ in range(9)]
Max = Max_i = Max_j = 0
for i in range(9):
    for j in range(9):
        if Arr[i][j] > Max:
            Max = Arr[i][j]
            Max_i, Max_j = i, j
print(Max)
print(Max_i+1, Max_j+1)
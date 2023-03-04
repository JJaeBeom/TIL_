'''
5 21
5 6 7 8 9
'''
'''
10 500
93 181 245 214 315 36 185 138 216 295
'''
N, M = map(int, input().split())
lst = list(map(int, input().split()))
Sum_lst = []
for i in range(N):
    for j in range(i+1, N):
        for x in range(j+1, N):
            Sum = lst[i] + lst[j] + lst[x]
            if Sum <= M:
                Sum_lst.append(Sum)
result = max(Sum_lst)
print(result)

# 21
# 497
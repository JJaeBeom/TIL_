# 20 7 23 19 10 15 25 8 13
# 7 8 10 13 19 20 23
N = 9
M = 7
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
A = sum(lst)
for i in range(N-1):
    for j in range(1, N):
        if lst[i] + lst[j] == A - 100 and i != j:
            a = lst[i]
            b = lst[j]
lst.remove(a)
lst.remove(b)
# for x in lst:
#     print(x)
print(*lst, sep='\n')
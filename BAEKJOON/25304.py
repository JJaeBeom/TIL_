X = int(input())
N = int(input())
total_cnt = 0
for i in range(1, N+1):
    a, b = map(int, input().split())
    sum_N = (a * b)
    total_cnt += sum_N
if total_cnt == X:
    print('Yes')
else:
    print('No')  
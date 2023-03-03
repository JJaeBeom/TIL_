'''
5
0 1 1 3 2
'''
N = int(input())
sequence = list(map(int, input().split()))
# print(sequence)
stu = [0 for _ in range(1, 101)]
# print(stu)
for i in range(len(sequence)):
    # stu[i], stu[stu[i]-sequence[i]] = stu[stu[i]-sequence[i]],stu[i]
    #stu[0] 1 , 1-0
    # stu[i], stu[i-sequence[i]] = stu[i-sequence[i]], stu[i]
    # stu[i] , stu[i-sequence[i]]
    a = i+1 - sequence[i]
    stu.insert(a-1, i+1)
for x in stu:
    if x != 0:
        print(x, end = ' ')
# stu = [_ for _ in range(1, 101)]
# stu1 = [_ for _ in range(1, 101)]
#
# for i in range(len(sequence)):
#     a = stu[i-sequence[i]]
#     stu1.insert(a-1, i+1)
# print(*stu1[:N])
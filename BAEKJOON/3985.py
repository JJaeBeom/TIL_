'''
10
3
2 4
7 8
6 9
'''

L = int(input())
N = int(input())
lst = [0] * 1000
guest = []
guest_1 = []
guest_2 = []
for a in range(N):
    P, K = map(int, input().split())
    for i in range(P, K+1):
        if lst[i-1] == 0:
            lst[i-1] = a+1
    guest_2.append(lst.count(a+1))
    guest.append(K-P)
# print(guest_2)
for x in range(len(guest)):
    if guest[x] == max(guest):
        guest = x+1
        break
for y in range(len(guest_2)):
    if guest_2[y] == max(guest_2):
        guest_2 = y+1
        break
print(guest)
print(guest_2)

# 출력
# 기대하던 방청객.
# 실제로 많이 받은 방청객.
# 여러명인 경우 번호가 작은사람출력
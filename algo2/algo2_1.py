# # 재귀 호출을 통한 순열 생성
# def perm(i, k): # i 값을 결정할 자리, k 결정할 개수
#   if i==k:
#     print(*p)
#   else:
#     for j in range(i, k): #자신부터 오른쪽 원소들과 교환
#       p[i], p[j] = p[j], p[i]
#       perm(i+1, k)
#       p[i], p[j] = p[j], p[i]

# p = [1, 2, 3]
# perm(0, 3)

# def perm(i, k): # i 값을 결정할 자리, k 결정할 개수
#   if i==k:
#     print(*p)
#   else:
#     for j in range(k): #사용하지 않은 숫자를
#       if used[j] == 0: #used에서 순서대로 검색
#         p[i] = A[j]
#         used[j] = 1 # j번 자리 숫자 사용으로 표시
#         perm(i+1, k)
#         used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸 수 있게

# A = [1, 2, 3, 3]
# p = [0] * 4
# used = [0] * 4
# perm(0, 4)


def perm(i, k): # i 값을 결정할 자리, k 결정할 개수
  if i==k:
    print(p)
  else:
    for j in range(k): #사용하지 않은 숫자를
      if used[j] == 0: #used에서 순서대로 검색
        p[i] = A[j]
        used[j] = 1 # j번 자리 숫자 사용으로 표시
        perm(i+1, k)
        used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸 수 있게

T = int(input())
for tc in range(1, T+1):
    A = list(map(int, input()))
    p = [0] * 6
    used = [0] * 6
    res
    cnt = 0
    B =perm(0, 6)
    if B[0] == B[1] == B[2]:
      cnt += 1
    if B[4] - B[3] == 1 and B[5] - B[4] == 1: 
      cnt += 1
    if B[3] == B[4] == B[5]:
      cnt += 1
    if B[1] - B[0] == 1 and B[2] - B[1] == 1: 
      cnt += 1
    
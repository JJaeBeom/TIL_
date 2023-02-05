N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
cnt = 0
# 리스트 요소로 접근
# for num in numbers: 
#     if v == num:
#         cnt += 1
# print(cnt)

# 리스트 인덱스로 접근
for idx in range(len(numbers)):
    if v == numbers[idx]:
        cnt += 1
print(cnt)
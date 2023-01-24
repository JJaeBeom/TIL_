# ###워크샵 02_ 2번
# favorite_food = {'치킨' : 20000, '피자': 25000, '햄버거': 15000}
# print(sum(favorite_food.values()) // len(favorite_food))

# ##워크샵 03_ 1번
# # 세로로 출력하기
# a = int(input('숫자를 입력해주세요. : '))
# for i in range(1, a+1):
#     print(i)

# ##워크샵 03_ 2번
# # 가로로 출력하기
# a = int(input('숫자를 입력해주세요. : '))
# for i in range(1, a+1):
#     print(i, end = ' ')

# ##워크샵 03_ 3번
# #거꾸로 세로로 출력하기
# a = int(input('숫자를 입력해주세요. : '))
# for i in range(a, -1, -1):
#     print(i)

# ## 워크샵 03_ 4번
# # #거꾸로 가로로 출력하기
# a = int(input('숫자를 입력해주세요. : '))
# for i in range(a, -1, -1):
#     print(i, end = ' ')

# ## 워크샵 03_ 5번
# # N줄 덧셈
# number = int((input('숫자를 입력해주세요. : ')))
# a = 0
# for i in range(0, number+1):
#     a += i
# print(a)

# ## 워크샵 03_ 06번
# # 삼각형 출력하기
# a = int(input('숫자를 입력해주세요. : '))
# for i in range(0, a+1):
#     b = (a-i)*' '
#     c = i*'*'
#     print(b, c)

## 워크샵 03_ 07번
# 중간값 찾기
numbers = [
85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24,
]
print(sorted(numbers))
print(len(sorted(numbers))// 2 + 1)
print(sorted(numbers)[17-1])
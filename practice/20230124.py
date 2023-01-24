# ##워크샵04_1번
# #간단한 N의 약수
# N = int(input('숫자를 입력해주세요. : '))
# for i in range(1, N+1):
#     if N % i == 0:
#         print(i, end= ' ')

# ##워크샵04_2번
# #List의 합 구하기
# def list_sum(numbers):
#     a = 0
#     for i in numbers:
#         a += i
#     return a

# print(list_sum([1, 2, 3, 4, 5]))

# ##워크샵04_3번
# #Dictionary로 이루어진 List의 합 구하기
# def dict_list_sum(a):
#     b = 0
#     for i in a:
#         b += i['age']
#     return b

# print(dict_list_sum([{'name': 'kim', 'age': 12},
# {'name': 'lee', 'age': 4}]))

# # ##워크샵04_4번
# # #2차원 List의 전체 합 구하기
# def all_list_sum(a):
#     b = 0
#     for i in a:
#         for j in i:
#             b += j
#     return b
# print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))

# ##아스키코드 워크샵 5번~7번
# ##워크샵04_5번
# #숫자의 의미
# def get_secret_word(a):
#     b= ''
#     for i in a:
#         b += chr(i)
#     return b
# print(get_secret_word([83, 115, 65, 102, 89]))

# ##워크샵04_6번
# #내 이름은 몇일까?
# def get_secret_number(a):
#     b = 0
#     for i in a:
#         b += ord(i)
#     return b
# print(get_secret_number('happy'))

##워크샵04_7번
#강한 이름
def get_strong_word(a, b):
    total_a = 0
    total_b = 0
    for i in a:
        total_a += ord(i)
    for j in b:
        total_b += ord(j)
    if total_a > total_b :
        return a
    elif total_a < total_b:
        return b
    else :
        return a, b
print(get_strong_word('z', 'a'))
print(get_strong_word('delilah', 'dixon'))
print(get_strong_word('zzz', 'zzz'))

        # = ''.join.(map())
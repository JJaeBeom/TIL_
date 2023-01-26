# 주어진 문자열에서 숫자, 문자, 기호가
# 각각 몇개인지를 판단하는 함수를 작성해보세요.

# def check(input_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0
    
#     for char in input_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         else:
#             symbol_count += 1
        
#     return char_count, digit_count, symbol_count

# input_str = "123#$%aiden_snow"   
# char_count, digit_count, symbol_count = check(input_str=input_str)
# print(f"char: {char_count}, digit: {digit_count}, symbol: {symbol_count}")

# 문자: 10개, 숫자 : 2개, 기호 : 7개 이런식.
#20230126 첫시간에 문제 풀이 해줌

# dust = {'key': 'value'}
# print(dust.get('samsung')) 
# print(dust.get('samsung', 'galaxy')) # none말고 디폴트값도 추가?
# #딕셔너리가 가지고 있는 메서드. 키값이 있는지 확인하고, 벨류를 반환하는 것
# #없으면 None을 반환
# print(dust['apple']) 
# #얘는 오류가 발생/ 오류가 발생해야되는 상황이 있을 것.

# dust = [1, 2, 3]
# print(dust.pop())
# # pop은 제거하는 애. 
# # 원본에서 값을 뺏다는 사실은 원본에서 확인 할 수 없다.
# # 그래서 pop은 값을 반환한다.

#################################################

# sample_list = [11, 22, 33, 55, 66]
# # 주어진 리스트의 3번 index에 있는 항목을 제거하고 변수에 할당해 주세요.

# print("original list: ", sample_list)

# elem = sample_list.pop(3)
# print('list after: ', sample_list)
# print('elem: ', elem)

# # sample_list의 가장 뒤에 77을 추가해보세요.
# sample_list.append(77)

# #할당해놓은 변수의 값을 sample_list의 2번 index에 추가해보세요.
# print(sample_list)
# sample_list.insert(2, elem)
# print(sample_list)

#########################################################

my_tuple = (11, 22, 33, 44, 55, 66)
#주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요.
new_tuple = my_tuple[3:5] #[3:-1]도 똑같이 동작.
print(new_tuple)

###################################################

##########람다###################
test_list = [1, 2, 3, 7, 4, 6, 5]
test_list.sort()
print(test_list)

scores = [('eng', 88), ('sci', 90), ('math', 80)]
# 정렬
print(scores)
scores.sort()
print(scores) #맨 앞에 있는 값을 기준으로 정렬되었다.
#
scores = [('eng', 88), ('sci', 90), ('math', 80)]
def check(x):
    return x[1]
# 정렬
print(scores)
scores.sort(key=check)
print(scores) #맨 앞에 있는 값을 기준으로 정렬되었다.

#####check 어차피 한번쓰고 안쓰잖아 그래서 람다쓰자.
scores = [('eng', 88), ('sci', 90), ('math', 80)]
print(scores)
scores.sort(key=lambda x: x[1])
print(scores)
#########################
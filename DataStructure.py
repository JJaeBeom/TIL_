# 주어진 문자열에서 숫자, 문자, 기호가
# 각각 몇개인지를 판단하는 함수를 작성해보세요.

def check(target_str):
    pass

# 문자: 10개, 숫자 : 2개, 기호 : 7개 이런식.
#20230126 첫시간에 문제 풀이 해줌

# dust = {'key': 'value'}
# print(dust.get('samsung')) 
# print(dust.get('samsung', 'galaxy')) # none말고 디폴트값도 추가?
# #딕셔너리가 가지고 있는 메서드. 키값이 있는지 확인하고, 벨류를 반환하는 것
# #없으면 None을 반환
# print(dust['apple']) 
# #얘는 오류가 발생/ 오류가 발생해야되는 상황이 있을 것.

dust = [1, 2, 3]
print(dust.pop())
# pop은 제거하는 애. 
# 원본에서 값을 뺏다는 사실은 원본에서 확인 할 수 없다.
# 그래서 pop은 값을 반환한다.
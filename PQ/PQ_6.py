dict = {}
print(dict.get('d')) # 없는 키 가져오라하면 None 반환
#########################################################
numbers = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        print(numbers[j][i], end=' ')
#########################################################
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다!')

    def eat(self):
        print(f'{self.name}!먹는다!')

dog = Animal('dog')
dog.walk()
#########################################################
lunch = ['짜장면', '짬뽕', '탕수육']

for idx, num in enumerate(lunch):
    print(idx, num)
    # 아래는 출력 예시입니다.
    # 0 짜장면
    # 1 짬뽕
    # 2 탕수육
#########################################################
"""
파이썬의 데이터 컨테이너는 크게 두가지 유형으로 나눌수 있는데 
각각, 시퀀스(sequence)형과 비시퀀스형(Non-sequence)이라고 부른다. 
이 중, 시퀀스형 데이터의 특징과 종류를 서술하시오.
시퀀스형 데이터란 순서가 있는 데이터형을 말한다. 단, 순서가 있다는 것이
정렬되어 있다는 것은 아니다. 시퀀스형 데이터에는 문자열, 리스트, 튜플, range가 있다.
시퀀스형 데이터는 인덱싱과 슬라이싱이 가능해야 한다. 
딕셔너리, 셋은 비시퀀스형 데이터다. 
"""

"""
지문의 코드를 실행하였을 때, 출력되는 결과와 그 이유를 서술하시오. 
만약, 오류가 발생한다면, 어떤 오류가 발생하는지 왜 발생하는지도 작성하시오.
"""
documents = ['java', 'python', 's5g4', 's5g2', 'spring', 'django', 'extra']
for i in range(0, len(documents), 2):
    print(i)
# python_class = [documents[i+1] for i in range(0, len(documents), 2)]

# print(python_class)
# IndexError: list index out of range 오류가 발생한다. 순회를 설정한 범위는 range(0, 7, 2)이다. 
# 즉, i는 0, 2, 4, 6을 순회하는데 documents[i+1]이 되면 마지막에 documents[7]이 되면서 리스트 범위를 벗어나게 된다.

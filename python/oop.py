class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
    def greeting(self):
        print(f'안녕하세요, {self.name}입니다.')

chulsu = Person('철수', '남')
chulsu.greeting() # 안녕하세요,철수입니다.


name = 'JB'
print(type(name)) # <class 'str'>
age = 20
print(type(age)) # <class 'int'>
# 사실 모든 것이 '객체'다.
# 붕어빵 틀이 int고 찍어낸 붕어빵 인스턴스가 20이다
# 만들어진 클래스를 가지고, 인스턴스를 만들고 있었다.
# 숫자 문자 리스트 셋 모두다 객체. 클래스의 인스턴스
# 

# class Person:
    # def __init__(self):
        # print('생성될 때 자동으로 불려요.')
# JB = Person()
class Person:
    def __init__(self, name, age):
        # print('생성될 때 자동으로 불려요.')
        self.name = name
        self.age = age
        
    def __str__(self):
        return '이 클래스를 하나의 문자열로 표현하면 이겁니다.'
JB = Person('JB', 20)
print(JB)
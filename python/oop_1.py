# # 데코레이터 예시
# # 이름(name)을 입력받아서 '안녕하세요, {}님!'을 출력하는 함수 ko_hello
# def ko_hello(name):
#     print(f'안녕하세요, {name}님!')

# def en_hello(name):
#     print(f'Hello, {name}!')
    
# def add_emoji(name, func):
#     func(name)
#     print('^~^//')

# add_emoji('JB', ko_hello)    
# add_emoji('JB', en_hello)    
# # ko_hello('JB') << 이렇게만 써도 됐었는데 오히려 길어졌어
# # en_hello('JB')
#################################################################
# def ko_hello(name):
#     print(f'안녕하세요, {name}님!')

# def en_hello(name):
#     print(f'Hello, {name}!')
    
# def add_emoji(name, func):
#     func(name)
#     print('^~^//')
    
# def emoji_decoratcr(func): #<< wrapper 함수를 
#     def wrapper(name):
#         func(name)
#         print('^~^//')
        
#     return wrapper

# new_func = emoji_decoratcr(ko_hello)
# new_func('JB')

# emoji_decoratcr(en_hello)('JB')
##################################################
#더 편하게 사용하는법. 데코레이터.
def emoji_decoratcr(func): #<< wrapper 함수를 
    def wrapper(name):
        func(name)
        print('^~^//')
        
    return wrapper



@emoji_decoratcr
def ko_hello(name):
    print(f'안녕하세요, {name}님!')
@emoji_decoratcr
def en_hello(name):
    print(f'Hello, {name}!')
    
# def add_emoji(name, func):
#     func(name)
#     print('^~^//')
    
ko_hello('JB')
en_hello('JB')
####################################################33
class MyClass:
    def method(self):
        return 'instance method' , self
    
    @classmethod
    def classmethod(cls):
        return '클래스 메서드', cls
    
    @staticmethod
    def staticmethod():
        return '스태틱 메서드'
    
my_class = MyClass()
print(my_class.method())
print(my_class.classmethod())
print(my_class.staticmethod())
############################################
class Person:
    def __init__(self):
        self._age = 0
   
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age


p1 = Person()
#p1._age = 25 # 이거 안됨
#print(p1._age) # 이거 안됨
p1.set_age(25)
print(p1.get_age()) #불편행,,
###############################################



class Person:
    def __init__(self):
        self._age = 0
   
    def get_age(self): #getter
        print('getter 호출 !')
        return self._age

    def set_age(self, age): #setter
        print('setter 호출 !')
        self._age = age

    age = property(get_age, set_age)

p1 = Person()
p1.age = 25
print(p1.age)

############################################
class Person:
    def __init__(self):
        self._age = 0
    
    @property
    def age(self): #getter
        print('getter 호출 !')
        return self._age
    
    @age.setter
    def age(self, age): #setter
        print('setter 호출 !')
        self._age = age

p1 = Person()
p1.age = 25
print(p1.age)
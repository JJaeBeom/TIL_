# def my_magic_func(n):
#     return n * 10


# my_list = [1, 2, 3, 4, 5]

# rlt = map(my_magic_func, my_list)
# print(list(rlt))

#1
# print((lambda x: x * x)(4))
# # 2
# rlt = ((lambda x: x * x)(4))
# print(rlt)
#3
# my_func = lambda n: n * 2
# print(my_func(2))
#4
def my_magic_func(n):
    return n * 10

map_obj = map(my_magic_func, [1, 2, 3])
rlt = list(map_obj)
print(rlt)
#5. #4를 람다함수로 바꿔보자.
map_obj = map(lambda n : n * 10, [1, 2, 3])
rlt = list(map_obj)
print(rlt)
#6. 재귀함수(자기 자신을 호출하는 함수)
# def recur():
#     print('뿅')
#     recur()

# recur()
#7. 재귀함수(팩토리얼 만들기)
def fac(n):
    if n == 0:
        return 1
    return n * fac(n - 1)

print(fac(5))
#8. 패킹/ 언패킹*

##x, y = 1, 2 #파이썬 입장에서 여기 두개있는거 각각 넣어달란거지? ㅇㅋ
##z = 1, 2, 3 #여기있는 값 다 퉁쳐서 넣어주면 되지? ㅇㅋ

## print(z, type(z))
# a, b = 1, 2, 3, 4 #<< 잉? a에 뭐넣으란거야 b에 뭐 넣으란거야 > 오류.
a, *b = 1, 2, 3, 4
print(a, b) #오~ 1, [2, 3, 4]
# a, b, *c = 1, 2, [3, 4]
##
def my_sum(a, b, c):
    return a + b + c

num_list = [10, 20, 30]
# rlt = my_sum(num_list[0], num_list[1], num_list[2])
rlt = my_sum(*num_list) ##<< 이렇게 쓰면 언패킹이 된다.

###이 패킹 언패킹을 함수로 적용해보면 마법같은 일이 일어남
def test(*values): #매개변수앞에 * 붙이면 매개변수를 가변적으로 받을 수 있는 함수를
    #만들 수 있다.
    for value in values:
        print(value)
test(1)
test(1, 2)
test(1, 2, 3, 4)

#가변인자.(사용자가 test라는함수를 사용할 때 몇개를 넣을지 잘모르겠는데 그거까지 다 처리해줄게)
def my_sum(*agrs):
    rlt = 0
    for value in agrs:
        rlt += value
    return rlt
my_sum() # 0
my_sum(1, 2, 3) #6
#변수 한개는 무조건 받아야겠다?
def my_sum(a, *agrs):
    rlt = 0
    for value in agrs:
        rlt += value
    return rlt
# my_sum() # 에러
my_sum(1, 2, 3) # 1은 a에 넣고, 나머지는 agrs에.

## 키워드 가변인자. **두개 붙여주면댐.
# test(1, 2, 3 ......)
# test(name= 'aiden', age=21, .....) 이렇게 쓰고싶을 때.
def test(**kwargs):
    print(kwargs, type(kwargs))
    kwargs['name']
    return kwargs

test(name= 'aiden', age=21)
##################################################
def test(*args, **kwargs):
    print(kwargs, type(kwargs))
    kwargs['name']
    return kwargs
####키워드들은 다 kwargs로, 1,2,3,4는 args로 들어감
test(1, 2, 3, 4, name= 'aiden', age=21, music='IU')
##################################################
#언패킹
def my_func(x, y, *z):
    return x, y, z
numbers = [1, 2, 3, 4, 5]
my_func(*numbers)
############가변인자가 가져갈 갯수를 정하는건 불가능. z 뒤에 a를 추가하고싶다면
def my_func(x, y, *z, a): #<< 여기에만 추가하면 안되고
    return x, y, z
numbers = [1, 2, 3, 4, 5]
my_func(*numbers, a=6)#여기에 추가하고 값 입력해야됨.
import random

# 1 ~ 45 숫자를 담은 list 생성
# range(n, m) = n부터 m-1 까지의 숫자를 생성

#numbers = range(1, 46) << 이거 x range(1, 46) 이렇게 나옴
numbers = list(range(1, 46)) # << 이거 o 

#numbers가 가진 숫자 중에 무작위 값을 하나씩 6번 뽑기
#리스트가 가지고 있는 값중 무작위 값을 뽑는 법은?


# while문을 사용하여 뽑아보기.

n = 0
while n < 5:
    print(random.sample(numbers, 6))
    n += 1

n = 0
for i in range(5) :
    print(random.sample(numbers, 6))





def sum(a, b):
    # code in here
    # while
    # if
    return a + b

num = sum(1, 3)
print(num)

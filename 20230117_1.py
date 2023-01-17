num = int(input("숫자를 입력해주세요: "))
if num % 2 == 1:  # if num % 2:
    print("홀수입니다")
else:
    print("짝수입니다")

a = 0
while a < 5:
    print("a")
    a = a + 1
print("끝")

for num in range(10):
    if num == 5:
        break
    print(num)

for num in range(10):
    if num == 5:
        continue
    print(num)

num = 5
if num == 0:
    pass
print(num)

dust = 80
if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

print('미세먼지 확인 완료')


num = 2
if num % 2 :
    result = '홀수입니다.'
else:
    result = '짝수입니다'
print(result)

num = 2
result = '홀수입니다.' if num % 2 else '짝수입니다'
print(result)

num = -5
if num >= 0:
    value = num
else:
    value = 0
print(value)

cnt = 100
cnt += 1
print(cnt)

cnt = 0
while cnt < 3:
    print(cnt)
    cnt += 1


grades = {'JB': 100, 'JC': 90, 'JD': 80}
print(grades.items())

number = int(input('숫자를 입력하세요: '))
n = 0
sum= 0
while n < number:
    n = n + 1
    sum = sum + n
print(sum)
print(f'1부터 {number}까지의 총 합은 {sum}입니다.')



[num**2 for num in [1,2,3] if num % 2]
[num for num in [1, 2, 3]]
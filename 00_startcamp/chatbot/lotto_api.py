import random
import requests


r = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049').json()
numbers = list(range(1, 7))
plist=[]

for x in range(6):
    plist.append(r[f'drwtNo{x+1}'])
print(plist)

# n = 0
# for i in range(6):
#     print()

# for _ in range(1000):
my_num = random.sample(range(1, 46), 6)
print(my_num)
my_num = [1, 2, 3, 4, 5, 6]
count = 0
for num in my_num:
        if num in plist:
            count += 1
if count == 6:
        print('1등')
elif count == 5:
        print('3등')
elif count == 4:
        print('4등')
elif count == 3:
        print('5등')
else :
        print('꽝')





# 4. 이걸 1000번 반복한다.
# 1. 로또 번호 6개를 추첨 받는다.
# 2. 내가 추첨 받은 6개의 번호가 1049회차 당첨 번호와 일치 하는지 확인한다.
    # 2-1. 확인하는 방법은 내 번호 6개를 순회하면서 
       # 1049회 당첨번호 목록에 해당 숫자가 있는지
       # 있다면 당첨 횟수 + 1
# 그래서 적중 횟수가 6개면 1등
# 5개면 3등
# 4개면 4등
# 3개면 5등
# 2개 이하면 꽝을 출력한다.
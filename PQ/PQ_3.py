import requests
print('역대 로또 당첨 번호')
회차정보 = input('회차를 입력해주세요 : ')
print(회차정보)
r= requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={회차정보}').json()
aa = []

for n in range(6) :
    aa.append(r[f'drwtNo{n+1}'])
print(aa)


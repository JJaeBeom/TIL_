import random #random은 모듈. 파이썬 파일 어디엔가 있다 = (컨트롤 + 클릭)하면 그 위치 찾아줌

menu = ['닭고기온메밀국수', '토마토 리조또', '무파마', '김치찜']
print(menu)
print(menu[0])

#print(dir(menu))
# print(dir(random))

print(random.choice (menu))
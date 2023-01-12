23/01/12

개발이 쉬워졌다. 

오픈소스 덕에

기술 이해만 있다면 누구든 활용 가능

Google Tensorflow - Airbnb, Xiaomi

Aws - Pinterest, Netflix

IBM watson - Legends, minter

컴퓨터 프로그래밍 언어

== 컴퓨터에게 무언가를 시킬 때 쓰는 말

파이썬(Python)

 쉽다

 강력하다

 많은 사람들이 사용한다 

### python의 문법

 ctrl + / = 현재 포커싱 되어있는 줄을 주석 처리/ 주석 해제

1. 저장 
   
   저장-변수(Variable) 하나의 값을 저장할 수 있는 저장공간  dust = 60 넣었다가 dust=50으로 변경 가능
   
   저장-List
   
   ```python
   menu = ['닭고기온메밀국수', '토마토 리조또', '무파마', '김치찜']
   print(menu)
   print(menu[0])
   ```
   
   ```python
   student = {'홍진환': 50, '김성현': 0, '홍진환':30}
   print(student)
   ```
   
   저장-딕셔너리> 이름표를 단 여러 개의 값을 저장할 수 있는 저장공간
   
   
   
    무엇을 저장하는가
   
      1)숫자                                                     현실세계에 존재하는 모든 숫자
   
   기본적인 연산이 가능
   
      2)글자                                                   현실세계에 존재하는 모든 글자
   
   따옴표로 둘러싼 글자or 숫자.
   
      3)참/거짓                                      True, False 단 두가지!  + None
   
   조건/반복에 사용됨                              300>200  =>true

##### 변수 활용하기

2. 조건
   
   if 만약 ~~라면
   
   else ~~아니라면
   
   ```python
   dust = 60 #dust = 60
   if dust > 50: #dust가 50보다 크다면
       print('50초과') #'50초과'를 출력해줘
   else: #아니라면
       print('50이하') #'50이하'를 출력해
   ```
   
   ```python
   dust = '60' #dust = 60
   if int(dust) > 50: 
       print('50초과') 
   else: #아니라면
       print('50이하') 
   ```
   
   elif 다중조건때 붙여준다. 하나의 조건을 통과하면 다음 조건은 안본다.
   
   ```python
   dust = 60
   if dust > 50:
       print('50초과')
   elif dust > 30:            #만약 elif가 아니라 if라면 50초과 30초과가 나옴
       print('30초과')            #elif라면 50초과만 나옴
   else:
       print('50이하')
   ```

3. 반복

       반복- while @ 

```python
while ㅇㅇ:
    ㅁㅁ
```

```python
#n이 0일때 
n = 0
#만약 n이 3보다 작다면 -> 조건을 만족하는 동안 아래 코드를 실행
while n < 3:
#계속 n을 출력하고,
    print(n)
#n에 1을 더해줘 > n에 1을 더하고, 그 값을 다시 n에 할당해 줘
    n += 1
```

       반복-for (여러 개의 값을 저장하는 변수에서 반복하여 값을 꺼내어 사용

```python
For (변수) in (순회가능한 변수들-리스트,딕셔너리 둘다 가능)


numbers = [1, 2, 3, 4]
# numbers 리스트가 가진 모든 요소를 순회 할때 까지
# num 이라는 변수는 정해진 이름? 아니다. -> 변수 이름 우리가 마음대로 지을 수 있다.zzz처
for zzz in numbers:
# numbers가 가진 각 요소를 출력
    print(zzz)
    ㅔ
    
```

| while 조건:    | for                       |
| ------------ | ------------------------- |
| 종료조건이 반드시 필요 | 정해진 범위를 반복하기에 종료조건이 필요 없음 |
|              |                           |



### VScode

- Vscode는 마이크로소프트에서 개발한 코드 에디터의 한 종류

- Windows, Mac, Linux를 모두 지원수업 내용

- 기존 개발 도구들 보다 가볍고 빠르고, 점유율이 높은 에디터

- 무한한 확장성
  
  - SSAFY에서 사용하게 될 python, html, css, javascript를 모두 다룰 수 있음.

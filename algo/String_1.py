# BruteForce
def BruteForce(p, t):
    i = 0 # t의 검색 인덱스(t에서의 비교 위치)
    j = 0 # p의 검색 인덱스(p에서의 비교 위치)
    # len(p) : 찾을 패턴의 길이
    # len(t) : 전체 텍스트의 길이
    while i < len(t) and j <len(p):
        # 비교할 문장이 남아있고, 패턴을 찾기 전이면
        if t[i] != p[j]: #서로 다른 글자를 만나면
            i = i - j   #비교를 시작한 위치로
            j = -1 # -1로 초기화(패턴의 시작 전으로)
        i += 1 # 같건 다르건
        j += 1 # i , j 하나씩 증가
    if j == len(p): #패턴을 찾은 경우
        return i - len(p) #위치 반환
    else: #못찾은경우
        return -1 # -1 반환
    
pattern = "Python"
text = "Hello Python World"
print(BruteForce(pattern, text))
###############################################
#BruteForce 부분합? 위에꺼랑 똑같이 나옴
def BruteForce2(p, t):
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            if t[i+j] != p[j]:
                break
        else:
            return i
        
pattern = "Python"
text = "Hello Python World"
print(BruteForce2(pattern, text))
############################################
##pattern이 몇개가 있는지 세는 것.
def BruteForce3(p, t):
    cnt = 0
    for i in range(len(t)-len(p)+1):
        for j in range(len(p)):
            if t[i+j] != p[j]:
                break
        else:
            cnt += 1
            #return i 중단하고 나가라고 했는데
    return cnt
        
pattern = "Python"
text = "Hello Python a Python World"
print(BruteForce3(pattern, text))
##################################################


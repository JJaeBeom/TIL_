# 2817_부분 수열의 합
#백트래킹: 가능한 모든 경우 => 답
#[1] 종료조건(n)    tree
# n : 숫자번호(index)
#[2] tree(시각적)
# 
def dfs(n, sm):
    global ans
    # [3] 가지치기: 더이상 정답 갱신 가능성 없는 경우. 
    # 가장 마지막에 해라, 가장 위쪽에.
    if K < sm:
        return
    
    #[1] 종료 조건(n에 관련된걸로 만들자): 반드시 정답처리는 여기서
    if n == N: 
        if sm==K:
            ans += 1
        return    
    #[2] 하부 호출
    dfs(n+1, sm+lst[n])# 포함
    dfs(n+1, sm)# 포함X

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    
    ans = 0
    dfs(0, 0)
    
    print(f'#{tc} {ans}')
# 1486_장훈이의 높은 선반

def dfs(n, sm):
    global ans
    # 최소값 구할때 항상(?) 성공하는 가지치기
    # if sm-B >= ans:
    #     return        
    
    # 
    if ans == 0: #이미 만점!
        return
    
    if n==N:
        if sm >= B:
            ans = min(ans, sm-B)
        return
    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    
    ans = N*10000
    dfs(0, 0)
    
    print(f'#{tc} {ans}')

# 1952_수영장[모의]

def dfs(n, sm):
    global ans
    if n> 12:
        ans = min(ans, sm)
        return
    
    dfs(n+1, sm+day*lst[n]) #일간권
    dfs(n+1, sm+mon) #월
    dfs(n+3, sm+mon3) #분기권
    dfs(n+12, sm+year) #년간
    

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    
    # [1] 백트래킹    
    # ans = 365 * 3000
    # dfs(1, 0)

    # [2] 규칙성 찾기
    s = [0] * 13
    for i in range(1, 13):
        # 가능한 방법 중 i달까지의 최소비용
        s[i] = s[i-1] + day * lst[i] #일간권
        s[i] = min(s[i], s[i-1]+ mon) #월간권
        if i >= 3:
            s[i] = min(s[i], s[i-3]+ mon3) #월간권
        if i >= 12:
            s[i] = min(s[i], s[i-12]+year)   
    
    ans = s[12]    
    
    print(f'#{tc} {ans}')
    
# 2819_격자판의 숫자 이어 붙이기

def dfs(n, tst, ci, cj):
    if n==7:
        sset.add(tst) # 중복 제거
        return
    
    for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<4 and 0<=nj<4:
            dfs(n+1, tst+arr[ni][nj], ni, nj)

T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    sset = set()
    
    for i in range(4):
        for j in range(4):
            dfs(1, arr[i][j], i, j)
    
    ans = len(sset)
    print(f'#{tc} {ans}')
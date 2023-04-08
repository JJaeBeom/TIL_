def bfs(s, e):
    #[1] 큐, v[], 필요 변수 생성
    global ans
    q = []
    v = [0] * ans
    #[2] 초기데이터 삽입, v[] 초기화

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)

        if c == e:
            ans = v[e] -1
            return ans 
        
        # 3방향, 범위 내(0~200000), 미방문
        for n in (c-1, c+1, c*2):
            if 0<=n<=200000 and v[n] ==0:
                q.append(n)
                v[n] = v[c]+1
    return -1    


N, K = map(int, input().split())
ans = 200001

bfs(N, K)
print(ans)

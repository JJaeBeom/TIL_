# 팩토리얼 (재귀)
N = int(input()) 
# 0보다 크거나 같은 정수 N
def fac(N):
    if N == 1 or N == 0: 
        #N이 1이나 0일 때 1반환
        return 1
    else:
        return N * fac(N-1)
print(fac(N))

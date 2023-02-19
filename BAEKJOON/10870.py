# def pibo(N):
#     if N < 2:
#         return N
#     else:
#         return pibo(N-1) + pibo(N-2)

# N = int(input())
# print(pibo(N))

########################
#메모이제이션 활용 - 백준에선 런타임에러 뜨넴
def fibo(N):
    global memo
    if N >= 2 and memo[N] == 0:
        memo[N] = (fibo(N-1) + fibo(N-2))
    return memo[N]

N = int(input())
memo = [0]* (N+1)
memo[0] = 0
memo[1] = 1
print(fibo(N))


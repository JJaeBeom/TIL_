# # 부분집합 구하기
# def f(i, k):
#     if i == k:
#         for j in range(k):
#             if bit[j]:
#                 print(A[j], end = ' ')
#         print(bit)
#     else:
#         bit[i] = 1
#         f(i + 1, k)
#         bit[i] = 0
#         f(i + 1, k)

# A = [1, 2, 3]
# N = len(A)
# bit = [0]*N
# f(0, N)


# # 부분집합의 합
# def f(i, k):
#     if i == k:
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j]

#         print(bit, s)
#     else:
#         bit[i] = 1
#         f(i + 1, k)
#         bit[i] = 0
#         f(i + 1, k)

# A = [1, 2, 3]
# N = len(A)
# bit = [0]*N
# f(0, N)

# # 연습문제 [부분집합의 합이 10인 ]
# def f(i, k, key):
#     if i == k:
#         s = 0
#         for j in range(k):
#             if bit[j]:
#                 s += A[j] #부분집합의 합
#         if s == key: #합이 key와 같은 부분집합을 출력
#             for j in range(k):
#                 if bit[j]:
#                     print(A[j], end = ' ')
#             print()
#     else:
#         bit[i] = 1
#         f(i + 1, k, key)
#         bit[i] = 0
#         f(i + 1, k, key)

# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(A)
# key = 10
# bit = [0]*N
# f(0, N, key)

#백트래킹 활용 합
def f(i, k, s, t): #i 원소, k집합크기, s i-1까지 고려된 원소의 합, t 목표
    global cnt
    global fcnt
    fcnt += 1
    if i == k:
        if s == t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            print()  
            cnt += 1
        return
    else:
        f(i+1, k, s+A[i], t) #A[i]포함
        f(i+1, k, s, t) #A[i] 미포함


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 50
cnt = 0
fcnt = 0
bit = [0]*N
f(0, N, 0, key)
print(cnt, fcnt) #합이 key인 부분집합의 수

#####################################################
def f(i, k, s, t): #i 원소, k집합크기, s i-1까지 고려된 원소의 합, t 목표
    global cnt
    global fcnt
    fcnt += 1
    if s > t: # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    if i == k:
        if s == t:
            cnt += 1
        return
    else:
        f(i+1, k, s+A[i], t) #A[i]포함
        f(i+1, k, s, t) #A[i] 미포함


N = 20
A = [i for i in range(1, N+1)]
key = 10
cnt = 0
fcnt = 0
bit = [0]*N
f(0, N, 0, key)
print(cnt, fcnt) #합이 key인 부분집합의 수

##########순열?
def f(i, k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            # p[i]결정, p[i]와 관련된 작업 가능
            f(i+1, k)
            p[i], p[j] = p[j], p[i]
            

p = [1, 2, 3]
N = len(p)
f(0, N)
#########################퀵정렬
def quickSort(a, begin, end) :
    if begin < end :
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
def partition(a, begin, end) :
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while(L<R and a[L]< a[pivot]) : L += 1
        while(L<R and a[R]>= a[pivot]) : R -= 1
        if L < R :
            if L == pivot : pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R



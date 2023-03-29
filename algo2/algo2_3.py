# # 병합 정렬
# def merge(left, right):
#     pass

# def msort(m):
#     if len(m) == 1:
#         return m
#     left = []
#     right = []
#     middle = len(m)//2
#     for x in range(m[0:middle+1]):
#         left.append(m[x])
#     for x in range(m[middle:]):
#         right.append(m[x])
    
#     left = msort(left)
#     right = msort(right)
#     return merge(left, right)        
    
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
    
#     msort(arr)
# #####################################################
# # 병합정렬
# def msort(m):
#     if len(m) == 1:
#         return m
#     middle = len(m)//2
#     left = m[0:middle]
#     right = m[middle+1:]
    
#     left = msort(left)
#     right = msort(right)
#     return merge(left, right)        
    
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
    
#     msort(arr)
######################################################
# 병합정렬 이거쓸까잉?
def msort(start, end):
    if start == end:
        return
    middle = (start+end)//2
    msort(start, middle)
    msort(middle+1, end)
    # merge()
    k = 0
    left, right = start, middle+1 # 왼쪽과 오른쪽에서 가장 작은 숫자의 위치
    while left <= middle or right <= end:
        if left <= middle and right <= end:
            if arr[left] <= arr[right]:
                tmp[k] = arr[left]
                left += 1
            else:
                tmp[k] = arr[right]
                right += 1
            k += 1
        elif left <= middle:
            while left <= middle:
                tmp[k] = arr[left]
                left += 1
                k += 1
        elif right <= end:
            while right <= end:
                tmp[k] = arr[right]
                right += 1
                k += 1
    
    i = 0
    while i < k :
        arr[start + i] = tmp[i]
        i += 1
    return         
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    msort(0, N-1)
    print(arr)
    
#####################################################################
# 퀵소트
def hoare(A, l, r):
    pivot = A[l] # 맨 왼쪽 원소 기준
    i = l        # 피봇보다 큰값을 찾아 오른쪽으로 이동
    j = r        # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:
        while i<=j and A[i] <= pivot: #교차되서 멈추거나, 피봇보다 큰 애를 만나서 멈춤
            i += 1 # 피봇보다 큰 애를 찾아서 오른쪽으로 감
        while i<=j and A[j] >= pivot:
            j -= 1 # 피봇보다 작은애를 찾아서 왼쪽으로 감
        if i < j: #교차하지않은 경우
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]
    return j
            

def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s-1)
        qsort(A, s+1, r)
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    qsort(arr, 0, N-1)
    print(arr)
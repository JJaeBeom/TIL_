#1 병합
# 분할 단계
def merge_sort(arr):
    if len(arr) <= 1:   # 길이가 1이 될때까지 분할하는거야
        return arr
 
    middle = len(arr) // 2  # 중심을 기준으로 두개의 구간으로 나누기
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)   # 병합 고고
 
 
# 병합 단계
def merge(left, right):
    global answer
 
    if right[-1] < left[-1]:    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 count
        answer += 1
 
    # pop(0) 대신 인덱스로 접근, append 사용
    result = []
    len_l = len(left)
    len_r = len(right)
    l = r = 0
    while l < len_l or r < len_r:       # left, right에 추가할 원소 남아있을 때까지 반복
        if l < len_l and r < len_r:     # left, right에 둘다 원소가 남아 있다면
            if left[l] <= right[r]:     # 왼쪽이 작은 경우
                result.append(left[l])  # 왼쪽 값 추가
                l += 1  # left의 다음 원소 지목
            else:
                result.append(right[r]) # 오른쪽이 작은 경우, 오른쪽 값 추가
                r += 1  # right의 다음 원소 지목
 
        elif l < len_l: # left에만 원소 남아있는 경우
            result.append(left[l])
            l += 1
        elif r < len_r: # right에만 원소 남아있는 경우
            result.append(right[r])
            r += 1
 
    return result
 
 
tc = int(input())
for idx in range(1, tc+1):
    n = int(input())
    arr = list(map(int, input().split())) 
    answer = 0
    result = merge_sort(arr)
    print(f'#{idx} {result[n//2]} {answer}')


def merge2(left, right):
global answer

if right[-1] < left[-1]:    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 count
    answer += 1

# 인덱스로만 접근
len_l = len(left)ㄴ
len_r = len(right)
result = [0 for _ in range(len_l+len_r)]
l = r = i = 0
while l < len_l or r < len_r:       # left, right에 추가할 원소 남아있을 때까지 반복
    if l < len_l and r < len_r:     # left, right에 둘다 원소가 남아 있다면
        if left[l] <= right[r]:     # 왼쪽이 작은 경우
            result[i] = left[l]     # 왼쪽 값 추가
            i += 1      # result 다음 자리로 이동
            l += 1      # left의 다음 원소 지목
        else:
            result[i] = right[r]    # 오른쪽이 작은 경우, 오른쪽 값 추가
            i += 1      # result 다음 자리로 이동
            r += 1      # right의 다음 원소 지목

    elif l < len_l:     # left에만 원소 남아있는 경우
        result[i] = left[l]
        i += 1
        l += 1

    elif r < len_r:     # right에만 원소 남아있는 경우
        result[i] = right[r]
        i += 1
        r += 1

return result


#2 퀵
def quick_sort(left, right):
    if left >= right:
        return

    pivot = left
    i = left+1 #피봇보다 큰 값을 찾아 오른쪽으로 이동
    j = right-1 #피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:
        while i <= j and A[pivot] >= A[i]: 
            # 교차되서 멈추고  피봇보다 큰 애 만나서 멈춤
            i += 1 #피봇보다 큰애 만나서 오른쪽으로 감
        while i <= j and A[pivot] <= A[j]:
            # 교차되서 멈추고 피봇보다 작은애 만나면 멈춤
            j -= 1 #작은애 만나면 왼쪽으로

        if i <= j: #교차하지 않은 경우
            A[i], A[j] = A[j], A[i]
    A[pivot], A[j] = A[j], A[pivot]

    quick_sort(left, j)
    quick_sort(j+1, right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(0, len(A))
    print(f'#{tc} {A[N//2]}')




#3 이진
T = int(input())
for tc in range(1, T+1):
    answer = 0
    N, M = map(int, input().split())
    # 이분탐색은 정렬을 기본조건으로 한다.
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    for b in B:
        # 중간을 탐색하기 때문에 최소점과 최대점을 잡아준다.
        min_idx = 0
        max_idx = N - 1
        # 왼쪽으로 갔는지 오른쪽으로 갔는지 체크하기 위한 용도
        flag = ''
        # 탐색범위가 같아지거나 엇갈릴때까지 반복한다.
        while min_idx <= max_idx:
            # 중간지점의 위치를 구한다.
            avg_idx = (min_idx+max_idx)//2
            # 중간지점의 값이 정답이라면 answer를 늘리고 반복문을 중지한다.
            if A[avg_idx] == b:
                answer += 1
                break
            # 선택한 인덱스 값이 찾는값보다 크다면
            elif A[avg_idx] > b:
                # 선택한 인덱스 위쪽은 필요없으므로 최대 인덱스 위치를 수정한다.
                max_idx = avg_idx - 1
                # 이전에도 왼쪽을 선택했다면 중지
                if flag == 'left': 
                    break
                # 왼쪽으로 갔다고 표시한다.
                flag = 'left'
            else:
                # 반대의 상황이라면 최소값을 바꿔준다.
                min_idx = avg_idx + 1
                # 이전에 오른쪽으로 갔다면 중지
                if flag == 'right': 
                    break
                # 오른쪽으로 갔다고 표시한다.
                flag = 'right'
    print(f'#{tc} {answer}')
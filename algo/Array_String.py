# #버블 정렬
# a = [7, 8, 9, 7, 6, 4, 5, 1, 3, 2]

# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]

# print(a)
# #################################################################
#카운팅 정렬
a = [7, 8, 9, 7, 6, 4, 5, 1, 3, 2]
# print(len(a))
a_count = [0] * 100
# 카운트 해주기
for i in range(len(a)):
    a_count[a[i]] += 1
# 누적카운트 계산
for i in range(len(a)-1):
    a_count[i+1] += a_count[i]
# 정렬
# 새로운리스트 b?
b = [0]*len(a)
# for i in range(len(a)-1, -1, -1):
for i in range(len(a)):
    # print(i)
    a_count[a[i]] -= 1
    b[a_count[a[i]]] = a[i]
print(b)
###################################################################
# #순열 만들기? 딱히..?
# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2 :
#                     print(i1, i2, i3)                    
###################################################################
arr = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]]
# #가로
# for i in range(3):
#     for j in range(5):
#         print(arr[i][j])
# #세로
# for i in range(5):
#     for j in range(3):
#         print(arr[j][i])
#지그재그
for i in range(3):
    for j in range(5):
        print(arr[i][j+(5-1-2*j)*(i%2)])
        # if i % 2 == 0:
        #     print(arr[i][j])
        # if i % 2 == 1:
        #     print(arr[i][-j-1])
#전치행렬 (가로 세로 바꿔줌) (근데 이 방법으론 행길이 열길이 같을때만 가능한듯?)
Arr =[[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for i in range(3):
    for j in range(3):
        if i < j:
            Arr[i][j], Arr[j][i] = Arr[j][i], Arr[i][j]
print(Arr)
# zip 써서 전치행렬 만들기. (검색해봄) #근데 zip은 짝 안맞으면 데이터 손실.
# Arr_1 = list(zip(*arr)) # list(zip(*이차원배열))
# print(Arr_1)
####
#델타 (2차배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법)



###################################################################
#비트연산자
#부분집합 생성 방법
arr = [3, 6, 7, 1, 5, 4]
n = len(arr) # 원소 개수
for i in range(1<<n): #1<<n은 부분집합의 개수
    for j in range(n): #원소의 수만큼 비트를 비교
        if i & (1<<j): #i의 j번 비트가 1인경우. #참고 (i&(1<<j))는 1인지 아닌지 검사하는 것
            print(arr[j], end=', ') # j번 원소 출력
    print()
print()
###################################################################
#이진탐색 (이진탐색을 위해서는 자료가 정렬된 상태여야 함)
def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end :
        middle = (start + end)//2 #중간.
        if a[middle] == key: #검색 성공
            return True
        elif a[middle] > key: # 미들값이, 키보다 클때,
            end = middle - 1
        else :
            start = middle + 1
    return False #검색 실패. 없다는 뜻
    # 재귀로 이진 탐색
###################################################################
#Gravity
#Baby-gin

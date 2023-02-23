def preorder(i):
    if i: #if i > 0 . 존재하는 정점이면
        print(i, end = ' ')
        preorder(left[i])
        preorder(right[i])
    return
# def preorder(i):
#     print(i, end = ' ') # 처음 들어온게 확실할 때? 이런식으로 쓸수는 있다.
#     if left[i]: 
#         preorder(left[i])
#     if right[i]:
#         preorder(right[i])
#     return   

V = int(input())
arr = list(map(int, input().split()))
E = V - 1
left = [0] * (V+1) #부모를 인덱스로 왼쪽자식 저장
right = [0] * (V+1) # 오른쪽 자식 저장
# child = [[] for _ in range(V+1)]
par = [0] * (V+1) #자식을 인덱스로 부모 저장 << 루트찾을때?
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p
    #child[p].append(c)

# root = 1
# while par[root] != 0: # root 찾기
#     root += 1
# print(root)
preorder(1)

#서브트리 안에서 순회시키면 그 안에꺼만 나옴.
#preorder(5) #5-8-9
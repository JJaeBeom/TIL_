# 트리
#                 C
#       B                   E
#   A       3           D          F
# 1    2             4     5     6     G
#                                     7  8

# 전위 순회 # C B A 1 2 3 E D 4 5 F 6 G 7 8
# 중위 순회 # 1 A 2 B 3 C 4 D 5 E 6 F 7 G 8
# 후위 순회 # 1 2 A 3 B 4 5 D 6 7 8 G F E C

# 전위 순회
def preorder(node):
    if node <= len(Tree)-1 :
        if Tree[node] != '0':
            print(Tree[node], end = ' ')
        preorder(node * 2)
        preorder(node * 2 + 1)
# 중위 순회
def inorder(node):
    if node <= len(Tree)-1 :
        inorder(node* 2 )
        if Tree[node] != '0':
            print(Tree[node], end = ' ')
        inorder(node* 2 + 1)
# 후위 순회
def postorder(node):
    if node <= len(Tree)-1 :
        postorder(node * 2)
        postorder(node * 2 + 1)
        if Tree[node] != '0':
            print(Tree[node], end = ' ')

Tree = ['0', 'C', 'B', 'E', 'A', '0', 'D', 'F', '0', '0', '0', '0', '0','0', '0' ,'G']
postorder(1)

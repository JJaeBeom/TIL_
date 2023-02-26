import sys

stack = []
# K = int(input())
K = int(sys.stdin.readline())
for _ in range(K):
    # k = int(input())
    k = int(sys.stdin.readline())
    if k != 0:
        stack.append(k)
    else:
        stack.pop()
result = 0
for i in stack:
    result += i
print(result)
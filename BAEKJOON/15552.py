import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

# rstrip() = 문자열 오른쪽에 있는 공백('')이나 개행문자('\n')을 제거하는 메서드.
# ex) sys.stdin.readline().rstrip()
# lstrip() = 왼쪽 제거 / strip() 양쪽 제거
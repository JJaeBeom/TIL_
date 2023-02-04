H, M = list(map(int, input().split()))
C = int(input())

if M + C < 60:
    M = M + C
    print(H, M)
else :
    H = H + ((M + C) // 60)
    M = (M + C) % 60
    if H >= 24:
        H = H - 24
    print(H, M)
N = int(input())
A = N // 10
B = N % 10

cnt = 0
while N < 100:
    C = (B*10) + ((A + B) % 10)
    if N == C:
        cnt += 1
        break
    A = C // 10
    B = C % 10
    cnt += 1
print(cnt)




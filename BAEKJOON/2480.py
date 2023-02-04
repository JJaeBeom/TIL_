A, B, C = list(map(int, input().split()))

price = 0
if A == B == C :
    price = 10000 + (A * 1000)
elif A == B or A == C or B == C:
    if A == B:
        price = 1000 + (A * 100)
    elif A == C:
        price = 1000 + (A * 100)
    else: 
        price = 1000 + (B * 100)        
else :
    price = max(A, B, C) * 100
    
print(price)
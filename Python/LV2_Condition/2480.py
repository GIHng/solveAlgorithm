A, B, C = map(int, input().split())

if A == B:  # A와 B가 같은 경우
    if B == C:  # A, B, C가 같은 경우
        print(10000 + A * 1000)
    else:  # A, B만 같은 경우
        print(1000 + A * 100)
elif (A == C) ^ (B == C):  # B, C만 같은 경우
    print(1000 + C * 100)
else:
    print(max(A, B, C) * 100)

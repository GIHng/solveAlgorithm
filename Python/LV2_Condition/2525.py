H, M = map(int, input().split())
T = int(input())

M = M + T
if M >= 60:
    H = H + (M // 60)
    M = M % 60
if H > 23:
    H = H - 24

print(H, M)

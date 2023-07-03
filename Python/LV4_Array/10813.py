N, M = map(int, input().split())
L = [0] * (N)

for k in range(N):
    L[k] = k+1

for _ in range(M):
    i, j = map(int, input().split())
    temp = L[i-1]
    L[i-1] = L[j-1]
    L[j-1] = temp

print(*L)
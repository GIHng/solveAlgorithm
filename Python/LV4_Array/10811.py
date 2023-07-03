N, M = map(int, input().split())

L = [i for i in range(1, N+1)]

for i in range(N):
    L[i] = i+1

for _ in range(M):
    i, j = map(int, input().split())
    temp = L[i-1:j]
    temp.reverse()
    L[i-1:j] = temp
print(*L, sep=" ")
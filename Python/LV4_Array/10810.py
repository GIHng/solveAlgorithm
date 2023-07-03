import sys

N, M = map(int, input().split())
L = [0] * (N)
for _ in range (M):
    i, j, k = map(int, sys.stdin.readline().split())
    for n in range (i-1, j):
        L[n] = k
print(*L)
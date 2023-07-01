import sys

N, X = map(int, input().split())

L = list(map(int, sys.stdin.readline().split()))

R = []
for i in L:
    if i < X:
        R.append(i)
    else:
        continue
print(*R)
L = list(map(int, input().split()))
R = [1, 1, 2, 2, 2, 8]

for i in range(len(R)):
    R[i] = R[i] - L[i]

print(*R, end=' ')
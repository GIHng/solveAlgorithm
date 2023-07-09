import sys
row = 0
col = 0
max = 0
M = [list(map(int, input().split())) for _ in range(9)]

for j in range(9):
    for k in range(9):
        if M[j][k] >= max:
            max = M[j][k]
            row, col = j+1, k+1
        else:
            continue

print(max)
print(row, col, sep=' ')

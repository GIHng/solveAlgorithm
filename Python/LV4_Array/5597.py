import sys

L = [0] * 30

for j in range(30):
    L[j] = j+1

for i in range(28):
    L.remove(int(input()))

print(*L, sep='\n')


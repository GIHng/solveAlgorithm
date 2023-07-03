import sys

L = []

for _ in range(9):
    input = int(sys.stdin.readline())
    L.append(input)

print(max(L))
print(L.index(max(L))+1)

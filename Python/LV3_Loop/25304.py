import sys

X = int(input())
N = int(input())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    X = X-(A*B)

if(not(X)):
    print('Yes')
else:
    print('No')

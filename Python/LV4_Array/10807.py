import sys
N = int(input())
L = list(map(int, sys.stdin.readline().split()))
v = int(input())
print(L.count(v))
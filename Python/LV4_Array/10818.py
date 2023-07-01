from sys import stdin

N = int(input())

L = list(map(int, stdin.read().split()))

print(min(L), max(L))
import sys

T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split()) # 여러 줄을 입력받을 때는 sys.stdin.readLine()을 사용해야 함.
    print(A+B)
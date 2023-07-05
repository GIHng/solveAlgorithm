T = int(input())

for _ in range(T):
    W, S = input().split()
    for i in S:
        print(i * int(W), end='')

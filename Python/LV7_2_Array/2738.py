A, B = [], []

N, M = map(int, input().split())

for i in range(N):
    num = list(map(int,input().split()))
    A.append(num)

for j in range(N):
    numB = list(map(int, input().split()))
    B.append(numB)

for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()

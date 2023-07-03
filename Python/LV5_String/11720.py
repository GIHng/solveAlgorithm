N = int(input())
S = input()
sum = 0
L = [0] * N
for i in range(0, N):
    sum += int(S[i])

print(sum)
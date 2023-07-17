number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = input().split()

N = ''.join(reversed(N))
sum = 0

for i in range(len(N)-1, -1, -1):
        sum += number.index(N[i]) * (int(B) ** i)

print(sum)
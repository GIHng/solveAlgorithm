import math

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(int, input().split())

result = ''
index = int(math.log(N, B))
for i in range(index,-1, -1):
    result += number[int((N/(B**i))%B)]

print(result)

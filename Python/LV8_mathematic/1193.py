N = int(input())

line = 1
while N > line:
    N -= line
    line += 1

if (line % 2) == 1:  # 홀수 줄이라면, <---
    print(line - N + 1, '/', N, sep='')
elif (line % 2) == 0:
    print(N, '/', line - N + 1, sep='')

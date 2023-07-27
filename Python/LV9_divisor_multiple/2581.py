M = int(input())
N = int(input())

l = []
for num in range(M, N+1):
    count = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            l.append(num)

if len(l) > 0:
    print(sum(l), min(l))
else:
    print(-1)

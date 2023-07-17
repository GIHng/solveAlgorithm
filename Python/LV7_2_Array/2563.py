N = int(input())
rect = [[0 for _ in range(101)]for _ in range(101)]

for i in range(N):
    width, height = map(int, input().split())
    for w in range(width, width+10):
        for h in range(height, height+10):
            rect[w][h] = 1
result = 0

for k in rect:
    result += k.count(1)
print(result)
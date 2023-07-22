# N, K = map(int, input().split())
# count = 0
# result = 0
# for i in range(1, N+1):
#     if N % i == 0:
#         count = count + 1
#         if count == K:
#             result = i
#             break
# print(result)


# -------------------------------------------------

N, K = map(int, input(). split())
l = []

for i in range(1, N+1):
    if N % i == 0:
        l.append(i)
try:
    print(l[K-1])
except:
    print(0)
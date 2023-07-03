# z -> 122, a ->97
# Word = [-1] * (122-97+1)
S = input()

for j in range(97, 122+1):
    print(S.find(chr(j)), end=' ')

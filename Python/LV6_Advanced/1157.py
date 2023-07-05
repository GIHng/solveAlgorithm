from collections import Counter
W = input().upper()
if W == ' ': exit()
W = list(W)

collection = Counter(W)
letter = collection.most_common(2)

if len(letter)==1:
    print(W[0])
elif letter[0][1] == letter[1][1]:
    print('?')
else:
    print(letter[0][0].upper())
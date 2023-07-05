croatiaWord = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
W = input()

for i in croatiaWord:
    W = W.replace(i, '*')
print(len(W))
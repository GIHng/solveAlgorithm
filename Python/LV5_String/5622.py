S = input()
R = 0
for i in S:
    if ord(i) >= ord('S'):
        i = chr(ord(i)-1)
        if ord(i) == ord('Y'):
            i = chr(ord(i)-1)
    R = ((ord(i)%65//3)+3)+ R
print(R)
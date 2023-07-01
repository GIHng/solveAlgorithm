A = int(input())

if (A%4==0) & ((A%100!=0) | (A%400==0)) :
    print('1')
else:
    print('0')
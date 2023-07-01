A, B = map(int, input().split())

# if (A >= 0) & ((B-45) >= 0) :
#     B = B - 45
# elif (A > 0) & ((B-45) < 0) :
#     B = 60 - (abs(B-45))
#     A-=1
# elif (A == 0) & ((B-45) < 0) :
#     B = 60 - (abs(B-45))
#     A = 23

B -= 45

if B < 0 :
    A -= 1
    B += 60
if A < 0 :
    A += 24

print(A, B)

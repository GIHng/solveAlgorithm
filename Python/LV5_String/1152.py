S = input()

R = S.strip(' ').count(' ')+1 if S != '' else 0
print(R)

# R = S.split(' ')
# result = len(R)
#
# for i in range(len(R)):
#     if R[i] == '':
#         result = result - 1
# print(result)
import sys
grade = ['A+','A0','B+','B0','C+','C0','D+','D0', 'P', 'F']
gradeScore = ['4.5', '4.0', '3.5', '3.0', '2.5', '2.0', '1.5', '1.0', '0', '0']

totalScore = 0
totalNum = 0

for j in range(0, 20):
    s, p, g = input().split()
    if g in 'P':
        continue
    totalScore += float(p) * float(gradeScore[grade.index(g)])
    totalNum += float(p)
if totalScore == 0:
    print('%.6f' % 0)
else:
    result = totalScore/totalNum
    print('%.6f' % result)
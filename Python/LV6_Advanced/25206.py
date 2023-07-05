import sys
grade = ['A+','A0','B+','B0','C+','C0','D+','D0', 'P', 'F']
gradeScore = ['4.5', '4.0', '3.5', '3.0', '2.5', '2.0', '1.5', '1.0', '0', '0']

totalScore = 0
totalNum = 0

L = []
for i in range(0, 20):
    L.append(input().split())
    if L[i][2] in 'PF'.split():
        continue
for j in range(0, 20):
    totalScore = totalScore + float(L[j][1]) * float(gradeScore[grade.index(L[j][2])])
    totalNum += float(L[j][1])

print(f"totalScore : ${totalScore} totalNum : ${totalNum} result : ${totalScore/totalNum}, totalNum, totalScore/totalNum")
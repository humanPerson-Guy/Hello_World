import score_analyzer_functions_cooper
testnames=[]
testScores=[]
totalScores=0
testScoreNum=int(input("how meny test scores do you whant to put in "))
for i in range(1,testScoreNum+1):
    testnames.append((input("input name")))
    testScores.append(float(input("input test score ")))


for l in range(0,testScoreNum):
    totalScores+=testScores[l]

avergeScore=totalScores/i
for x in range(testScoreNum):
    
    print(score_analyzer_functions_cooper.grade_giver(testnames[x],score_analyzer_functions_cooper.grade(testScores[x]),testScores[x]))

    x=x+1
    
 
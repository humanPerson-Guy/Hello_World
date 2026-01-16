import score_anilizer_function_cooper
totalScores=1
testScores=[]
failing=1
passing=1
failing=1
passing=1
testScoreNum=int(input("how meny test scores do you whant to put in "))
for i in range(0,testScoreNum+1):
    testScores.append(float(input("input test score ")))
    print(testScores)
    for l in range(1,testScoreNum,1):
        totalScores+=testScores[0]
    print(totalScores)
    avergeScore=totalScores/l
    print("class averge"+str(avergeScore))
    passing=0
    failing=0
score_anilizer_function_cooper.grade()

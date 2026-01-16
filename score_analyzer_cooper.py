testScores=[]
totalScores=0
testScoreNum=int(input("how meny test scores do you whant to put in "))
for i in range(1,testScoreNum+1):
    testScores.append(float(input("input test score ")))
print(testScores)
for l in range(0,testScoreNum):
    totalScores+=testScores[l]
print(totalScores)
avergeScore=totalScores/i
print("class averge"+str(avergeScore))
passing=0
failing=0


for r in range(0,testScoreNum):
    if testScores[r]>= 70:
        passing +=1
    else:
        failing +=1
print(str(failing) + "scores are failing and" + str(passing) + "scores is passing")


if avergeScore >=90:
    print("acseptible")
elif avergeScore>= 80:
    print("not even an A avrege ")
elif avergeScore>=70:
    print("passing but just barily should study more")
else:
    print("the scores where terrible thay should studty more")
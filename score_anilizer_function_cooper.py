testScores=[]
totalScores=0
testScoreNum=0
avergeScore=0
failing=1
passing=1
def grade():
    testScores=[]
    totalScores=0
    testScoreNum=0
    avergeScore=0
    failing=1
    passing=1
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


    
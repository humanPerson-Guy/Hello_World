studentGrade=int(input("enter student grade "))#entor sudent grade here
grade_statement="your student got a "#the messege you get befor the grade
if studentGrade >= 90:
    print(grade_statement+"A")#prints the letter grade you got
elif studentGrade > 79:
    print(grade_statement+"B")
elif studentGrade > 69:
    print(grade_statement+"C")
else:
    print(grade_statement+"F")


def grade(score=70):
       
    if score>= 90:
        return "A"
    elif score>= 80:
        return "B"
    elif score>= 70:
        return "C"
    else:
       return "F!"



def grade_giver(name,letter,score):
    return [name,letter,score]




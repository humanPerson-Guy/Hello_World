Gina=[93.5,"Gina"]
Charles=[98,"Charles"]
Will=[96,"Will"]

period1=["Tony",Gina[1],"Jake","Scully"]#the 124 piriods chidren
period3=["Amy","Santi",Charles[1],"Rosa"]
period4=[Will[1],"George","Nancy","Shawn"]
top_scores=[Gina[0],Charles[0],Will[0]]
top_sutdents=[]
top_sutdents.append([period1[1]])#adds top sudents to list
top_sutdents.append([period3[2]])
top_sutdents.append([period4[0]])

print("First period Students",period1)
print("First period Students",period3)#print all sudents names
print("First period Students",period4)


print("===")
print("Top students list",top_sutdents)#prits top sudents and thar scores
print("Top scores:",top_scores)

print("===")

print(Charles)
print("Charles scord",Charles[0])#tells ech top studnts score with thare names
print(Gina)
print("Gina scored",Gina[0])
print(Will)
print("Will scored",Will[0])
print("===")
top_scores_combinde=top_scores[1]+top_scores[2]+top_scores[0]#combins top scores
print("Average top score",top_scores_combinde/3)#Pirts top scores acros all classes
print("Average top score across all classes",top_scores_combinde/3)
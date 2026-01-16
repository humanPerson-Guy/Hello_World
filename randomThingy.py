stick=[1,0,0]#0 is damege 1 is mana cost 2 is self damege
cry=[1,1,-2]
punch=[2,0,0]
sword=[4,1,0]
super_sword=[8,3,0]
murder_everything=[5,12,13]
fireBall=[7,2,2]
fire=[1,2,0]
hp=1
sacrifice_damege=hp*3-1
infurno=[5,10,0]
sacrifice=[sacrifice_damege,18,hp-1]
flame_wall=[0,4,4]
obliterate=[999999999999999999999,30,9999999999999999999999999999]
balls=[1,0,0]
maxhp=9




clas=3
while clas!= "mage" and clas != "fighter" and clas != "smallchild" :
    clas=input(" chouse your class mage,smallchild,fighter")#pick your class
    print(clas)
    if clas == "smallchild":
        maxhp=15
        damegeModifyer=0
        attacks=[stick,cry]
        max_mana=3
        print("the weakest class for the hardest chalenge")
    elif clas == "fighter":
        print("chiken")
        maxhp=30
        damegeModifyer=2
        max_mana=15
    elif clas =="mage":
        print("you stinky")
        maxhp=20
        damegeModifyer=5
        max_mana=30
    print(maxhp,max_mana)

enimyhp=30

input("Wich attack you chouse")






letter=input("Veuillez saisir lettre:")
dimensions = int(input("Veuillez me donner une dimension (une taille):"))
topLigne = 0
topColonne = 0
colonne = 0

# condition pour saisir nombre positif
while (dimensions <= 0):
    dimensions = int(input("Attention!!! veuillez saisir un nombre entier positif superieur à zéro:"))
#le damier

while(topColonne < dimensions):
    topLigne= 1
    if(topColonne % 2 == 0) and (dimensions%2 ==0):#si nbre paire
        topLigne = 2
    elif(topColonne % 2 == 0) and (dimensions%2 !=0):# si nbre impaire
        topLigne = 0

    while(topLigne <= dimensions):
        if (topLigne % 2 == 0):
            print(letter, end='')
        else:
            print(" ", end='')
        topLigne += 1
    print("")
    topColonne += 1


#saut de ligne
print("")

    #la spirale à corriger...
while(colonne<dimensions) :
    ligne=0
    debut=0
    fin=(dimensions-1)
    while(ligne<dimensions):
    
        if(colonne %2 == 0):
            
            if((ligne>debut)and(ligne<fin)):
                print(" ",end='')
            else:
                print(letter, end='')
        
        else:
            debut=1
            fin=(dimensions-2)
            if((ligne==debut)or(ligne==fin)):
                print(" ",end='')
            else:
                print(letter, end='')

        ligne+=1
        debut +=1
        fin -= 1
    print("")
    colonne += 1

 
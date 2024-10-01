#Exercice 11
def probabilites_phrase(phrase):
    l = len(phrase)
    res = 0
    #Compteur d'occurences des lettres dans la phrase
    cptdict = dict()
    for k in phrase :
        if k in cptdict : cptdict[k]+=1
        else :  cptdict[k]=1

    #Calcul de la probabilité :
    for k in cptdict :
        res+=(cptdict[k]/l)*((cptdict[k]-1)/(l-1))
    print(res)


probabilites_phrase("bonjourjesuisunephraseenminusculesansespaces")
probabilites_phrase("cameo")
probabilites_phrase("pepe")
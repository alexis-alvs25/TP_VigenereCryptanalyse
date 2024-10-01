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
    print("K = ",res)
    return res

def friedman(cypher):
    Kr = 1/26 #Random distribution
    Ke = 0.067 #English Language
    K = probabilites_phrase(cypher)
    L = (Ke-Kr)/(K-Kr)
    print("L = ",L)


def analyse_frequentielle(cypher,L) :
    print(int((len(cypher)-(len(cypher)%L))/L))
    decoupage = [[] for _ in range(0,int((len(cypher)-(len(cypher)%L))/L))]
    #Découpage de boucher car si la phrase
    #est assez longue cela ne changera pas les occurences
    for i in range(int((len(cypher)-(len(cypher)%L))/L)):
        decoupage[i] = cypher[(i*L):(i*L)+L]
    print(decoupage)
    

probabilites_phrase("bonjourjesuisunephraseenminusculesansespaces")
probabilites_phrase("cameo")
probabilites_phrase("pepe")

print("Test de friedman 1: ")
# m=helloiambenjaminilovechocolate
# c=uwu
friedman("baffkcuivyjduichefirywdiwkfupy")

print("Test de friedman 2: ")
# m = helloiamanenglishsentencewithalotofwordsinitandeventhoughmynameisbenjaminiamold
# c=c
friedman("jgnnqkcocpgpinkujugpvgpegykvjcnqvqhyqtfukpkvcpfgxgpvjqwijoapcogkudgplcokpkcoqnf")

# m = hereisanexampleofaverylongcoherentenglishsentencethatcontinuestogrowwithoutanyspacesorpunctuationanditisimportanttonotethattheprocessofreadingthissentencecanbecomechallengingasthelackofspacesbetweenwordsrequiresyoutocarefullyparseeachwordinthecontextofthesentenceandastheletterscontinueonwardyoumightfindthatyourmindstartstobuildapatterninthewaythatyoureadthesewordswhichcangreatlyaidintheprocessofdecodingwhatisotherwiseafairlycomplexstringoftextasitgoesonandonthegoalhereistocreateaphraseofsignificantlengththatcanbothbemindbendingandinterestingwhilesimultaneouslyfollowingtheguidelinesthathavebeenprovidedinthisrequestyoumayalsonoticethattheabsenceofpunctuationleavesnoroomfortraditionalgrammarorsyntacticstructuringbutregardlessyouwillhopefullystillfindthatthissentenceisholdingontoitscoherenceevenasitstretchesfurtherandfurthertochallengethelimits
# c = iamakey

analyse_frequentielle("pedeswyvejawtjmorafipglanqgmpedexxcvgxiclqmnfexgcbhmtmslbizuowrwgdogagbhaudelgsbamiqwrbuxgrcafiyryvdutswgupardelbtanyxcbhmtdlcxracowqwfdekhgvgfhswqmnfexgckazbogmueohkpjmnsixkyatteveasorszeamsnedacmniobhqzecusvcayaudsairqfepjgpmrcicictwyvbqnfhogmvtqxdsdbhqsorrmnoekrbisfhopcbtqrcgmvtuneimvwmrncmcmugrxdqnptrergogrwmllsfabxqbonuspbipmtdipviztriuiyfhkxwwudekhrpeeegsplsihsgfkazgbiyblkashgvttezvmkeesyjbmcadsreehmtswmbhqrgmqmarasvjgcamzpcfsfrsrewffehxyaifgyiqwnmnnslbhqgyejpedeswrwcdekxciptrkwcwfeiqrgnioaxxjmnstrxfitoaxfmbhnewmllbqnnmloazdsrrmrqsdmlowtiviqqmgldelmogsvcdwlxogmlotteqyglexixiqbhmtretmbqextpwvudohgvtticvcyuqsdcmcmmykpqwnatsgcbhmtdlcibeexgcwfbuxgrcafiyrjmahecrmzoampspbrmdsxgwnmlqvyummryvqgnfamxgksfregrcrunqfsbrqgkvbteesisseixlrsnmfglvcqbixlpmllttadxfqseexxcvcqiclmtdunqslboutcgmpedexgcmvqnkwgbsfroxapeefevrpedaxhdcrfhovrwctavpcvgqtrijqmutc",7)
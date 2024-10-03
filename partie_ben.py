import math


#Exercice 11

#Compteur d'occurences des lettres dans la phrase
def compteur_occurences(phrase):
    cptdict = dict()
    for k in phrase :
        if k in cptdict : 
            cptdict[k]+=1
        else :  
            cptdict[k]=1
    return cptdict

#Calcul de la distribution des lettres dans la phrase
def probabilites_phrase(phrase):
    l = len(phrase)
    res = 0
    cptdict = compteur_occurences(phrase)
    #Calcul de la probabilité :
    for k in cptdict :
        res+=(cptdict[k]/l)*((cptdict[k]-1)/(l-1))
    print("K = ",res)
    return res

#Friedman compare la distribution des lettres à la distribution de la langue du message pour estimer la taille de la clé
def friedman(cypher,Ke = 0.067):
    Kr = 1/26 #Distribution aléatoire
    K = probabilites_phrase(cypher)
    L = (Ke-Kr)/(K-Kr)
    print("L = ",L)
    return L


def analyse_frequentielle(cypher,L,most_used_letter = 'e') :
    #Création de sous parties codées avec la même lettre
    dec = ["" for _ in range(L)]
    for i in range(0,(len(cypher)-len(cypher)%L),L):
        for j in range(L):
            dec[j]+=cypher[i+j]

    #On regarde la lettre qui apparaît le plus dans chaque sous séquence
    #On regarde le décalage entre elle est la lettre la plus utilisée dans notre message
    #Le décalage aura de grande chance de donner l'indice de la lettre utilisée pour chiffrer la sous partie !
    for i in range(L):
        occ = compteur_occurences(dec[i])
        v = {k for k in occ if occ[k] == max(occ.values())}
        first_letter = v.pop()
        index_fl = ord(first_letter) - ord('a');
        index_lang = ord(most_used_letter) - ord('a');
        decalage = ((index_fl - index_lang + 26) % 26) 
        print(i+1,"e lettre de la clé : ",chr((decalage)+ord('a')))
    
    

#probabilites_phrase("bonjourjesuisunephraseenminusculesansespaces")

#Friedman n'est pas très précis pour des petites phrases !
print("Test de friedman 1: ")
# m=helloiambenjaminilovechocolate
# c=uwu
friedman("baffkcuivyjduichefirywdiwkfupy")
print("Test de friedman 2: ")
# m = helloiamanenglishsentencewithalotofwordsinitandeventhoughmynameisbenjaminiamold
# c=c
friedman("jgnnqkcocpgpinkujugpvgpegykvjcnqvqhyqtfukpkvcpfgxgpvjqwijoapcogkudgplcokpkcoqnf")



print("=======ANALYSE FREQUENTIELLE=======")
# m = hereisaverylongsentenceinenglishthatwillreachabouttwothousandcharactersanditwillcontinuetoflowwithoutanyspacesorpunctuationwhatsoeverasyourequestedthechallengehereisnotonlytoreadthetextbutalsotoseehowyourmindnaturallyadjuststoparseeachindividualwordandfigureoutitsmeaningdespitebeingpresentedinaconstantunbrokenstringoflettersnowasthissentencegrowsitbecomesmoredifficulttoprocessbutwithsomefocusyoucanstillfinditpossibletoextractmeaningfromitthissentenceisdesignedtocontinuouslyexpanduntilwereachthetargetofaroundtwothousandcharacterswhilemaintainingcoherenceandmeaningthissortofexerciseisactuallyquitedemandingforyourbrainasitforcesittoprocesslettercombinationsinanunusualwaynormallywedealwithspacespunctuationandothercueslikespacingtosupportourofunderstandingbutnowwithoutthoseaidswearefacedwithachallengingtaskofunderstandingbymentallyseparatingwordsnowletscontinuewiththesentencegettingevenlongerandlongerasitisnecessarytoachievethedesiredlengthwithoutsacrificinganymeaningatallintheprocesseventhoughthismayseemlikeastressfulwaytoreaditdemonstratesaninterestingaspectofhumancognitiveskillsyourbrainisabletocopewiththeabsenceofspacesandstillidentifythestructureofthewordsweuseinhumanlanguagenowasthecharacterskeepincreasingthereisstillacleargoalofreachingatotalofaroundtwothousandcharactersinthesingleuninterruptedstreamthismeansthatwemustcontinuethephrasewithoutspacesorevenusingpunctuationtobridgethedifferentsectionsorideasofthemessageonceanideaisintroducedweshiftseamlesslyintothenextideawithoutanyneedtostoporpauseforthetexttokeeponfunctioningintuitivelyhoweverthisexperimentalsentenceshowswhatcaneventuallyhappenwhenournormalreadinghabitsarechallengedinnewwaysyoulllikelyfindyoudevelopabettercapacitytoparsethesechunksoflettersonceyougainmomentuminreadingthetextandyoumightfindthattheharderthetextistoreadthemorefocusedyourmindbecomesasitstrivestocorrectlyidentifyallthewordsnowtocontinuetowardsthetargetoftherequirednumberofcharacterswecankeepaddingmoreandmorewordstotheoveralllengthensuringwehavethesameconsistentlevelofcoherencethroughoutwhiletheresnocleardivisionhereyoucannoticethattherearestillcertainpatternsinthesentencethatmaketheevolutionofthetextmorepredictableallowingyourcognitiontofillinthegapsbetweenwordseventhoughnospacesareactuallybeingusedastheparagraphlengthensitalsoservesasaproofthatreadersadaptoverconsiderabletimeperiodswhenfacedwithunfamiliarpresentationsoftextthiscognitiveflexibilityisnoteworthybecauseitalsohighlightsourinnatecapacitytolearnandadapttonewchallengesasweapproachtwothousandcharacterswemustcontinuetheflowofthetextaddingmoredescriptioninsuchawaythatmeaningisneverlostandcoherenceisalwaysmaintaineddespiteanydifficultiespresentedinmaintainingthissteadyflowyoucancontinuetoreadthroughsmoothlynowaswesteadilypushfurtherthroughthelimituntilwereachourgoal
# c = iamakey
approx_key = friedman("pedeswydedyvslosqndilkeunoretiehdlybwulvvcictalssbtiodlmcsmnngfirmcdipaazdsxuqlxcyrrqngedsdtoiwsxfwufaxcqxaoecspxuzcdyybianglybsaefipiskoevcyuqsdibbhqcrejtezgolczeusxsrwnxydspmaptrirmxfbexytsatywcmhawisszmunnrybudavpwidvucxqbobabwcmaohsrbqvudeejeoddkrbnisubimctutcqcinunqhcaputofcqnspbiqmnfenmlicancxyvtgnlvmsezsdvgvgafvirbedsxsuisfhswqmnfexgcorawcmrjeoowiquodenmdniouvxrwpdomiqabgtgmrpsamojmkueyyyainetspjnizdsxnwseilpcboqxdvyktyekrgvgrryqgbtticwcvtqnmigadqssklmdfomslbizuyyqtyqxzelluztspumrqamlrpefabkcborabssvdfwyxfwueaxhapadamxczsihspcuaundegvizgmsfmrqnmiyvdyekrgvgfhswqwrfopivmroicigaaoteejtycusxcleyaxhgvgrobcmcrnrkmlisutpspkeeidxmxracowqteftovawmnixerqozssryvuzucyytwmyxspuaxliaclemlgmrpsbamiqxuzcdyybiankrbwttebgsmsxiuiqxaoixkrwsgpzspbogryjsvdqrcxyvdunqfsbnawgmrpogtdlmaeminwumadepeamdiidlykhmlviloizgdeqsoruxhczsfaxhgvgnywilbaxliwcxadadmlowarnwlwwxedwawnfixyceifhdlcaeztoramgqtdmloehexpmvgqrkrbtozgovyaificrckeeskvwbomcrmcdefhohcaidenpcvgfhgmrpogtceazirimmloazywiyvizgkxytlundlcxracowqmvqndlmcgttrmquaksoiktiwekwrzeespyjeaktyvcidutnikwnetbermsmnsrrmrqsdmloaepogrwftuwelkosnsxgdeekspjayaubfpiiziceztefomsnmwutrxfmansoramorszeamsmnnwrqlxinilbirydlcatdumxszeafdlceoddcaccsqixlsuazlkrecasexsuisfhogfirmcdipakqezmlkrqacmlottebigasfivpyklqabkmilafbiykhunqerwtmlyjyzognnxuwttoewyvdohkvyktqrcmlbhqssretegnsrrmrduzxclsfroekbhuswiyvsfhkxummgsdgmvtuneirpebhbeqmwutrssbsbamiqwrqvorsaizgzylktgadmmvtabbmboefhohgnfqrorraeotsslaodiniyaortrikmseaqimvcqaxmbmaussrrzopumibeeehsjraemmviqalkixxmbhqnobrqdqagmrpogtkrwveqddsqbobobtycsqfyvrpefehxrwkqezslnuzcdmmvizgsrrcififijghawozcztticivxediwilbaxsorrmnoeclmesihkxainqvorrcaxlilyxpqnglcvogrxspuaxroebqnshkfgbsmrogfilxexkcliznoauiyeyyyjtlukopwnizdisslehevsnibqtdipkabammrgtapkvqmtteciapuzkcsdteftovqwnoeissoaunwskmnfuwmlzemdsrebhqtobrinpyyykqgttpmllttadxfmhmrnipbhqtobrqsfobiylttewspmfacewclyaubqgvdnemskmsmssxqbruvowrwcarbiablkinilbirykpjbhqwyvbanawdsawnfixycboiabhqbhqtkvemtafdlczecusvclngmlipwfohkvyktqrcackazkoinidpixkkwrqaxhkwrqwyvbatatrimdedavpjmnstrilaudixkumhmvoxfmsmmogmvsusdilblqvopmncahovcvcqtrvmcgtoexupixedlczeenygjmaddszgaianripmyaumelvofimirpaftripmadecxgtloebxyqnbadxczneixxfmsqndilkefhkxkikqtricdoxudmmvortrirmxfmyvcxrqdsgribxekpjwwunqcmcrooqrgbiandsdqlxixxfmgmpcfcbwqexamzdeefilbhauqllwsbamiqirqamxsilxyligvggsohyattezepigdazljmnstrilaifavwmaedvowyaabrysdbhmtbiyledskhyxtavovawneinipibxedmkmpqrssbawtexjykepwsxfcnrawmjqadpbiqmnfadmmvsafdivbtticgmonutszcnlqxsfgtifyswlwtqwyvrpynemesaeutkpqwhugrpgohfsyypqnzadiaipmcsxwboxekvlinpanenbtanoaapaxloremsmsgiyxpdokgfbwatrssaazdmlyzaotovqeeyucxawnfixycbhqfvsuwffhoxcftmdnmlomarohcacdizxgwnuncyapaiaixfityekrgvgusxitmrxocxyvdooripmnoeswytwmycqyqnfasrcldqszmrmazynmdniouvxgmsbrowcvtqdsrkiiztkmlqnstrmqatqancdtoiyyyainooxxgvuqtyvcidfhbssohemysrplknyayawqsdiylixyzyqpfgrdlczttryyepttevmkqtgndmjeedekgfwudgyej")
analyse_frequentielle("pedeswydedyvslosqndilkeunoretiehdlybwulvvcictalssbtiodlmcsmnngfirmcdipaazdsxuqlxcyrrqngedsdtoiwsxfwufaxcqxaoecspxuzcdyybianglybsaefipiskoevcyuqsdibbhqcrejtezgolczeusxsrwnxydspmaptrirmxfbexytsatywcmhawisszmunnrybudavpwidvucxqbobabwcmaohsrbqvudeejeoddkrbnisubimctutcqcinunqhcaputofcqnspbiqmnfenmlicancxyvtgnlvmsezsdvgvgafvirbedsxsuisfhswqmnfexgcorawcmrjeoowiquodenmdniouvxrwpdomiqabgtgmrpsamojmkueyyyainetspjnizdsxnwseilpcboqxdvyktyekrgvgrryqgbtticwcvtqnmigadqssklmdfomslbizuyyqtyqxzelluztspumrqamlrpefabkcborabssvdfwyxfwueaxhapadamxczsihspcuaundegvizgmsfmrqnmiyvdyekrgvgfhswqwrfopivmroicigaaoteejtycusxcleyaxhgvgrobcmcrnrkmlisutpspkeeidxmxracowqteftovawmnixerqozssryvuzucyytwmyxspuaxliaclemlgmrpsbamiqxuzcdyybiankrbwttebgsmsxiuiqxaoixkrwsgpzspbogryjsvdqrcxyvdunqfsbnawgmrpogtdlmaeminwumadepeamdiidlykhmlviloizgdeqsoruxhczsfaxhgvgnywilbaxliwcxadadmlowarnwlwwxedwawnfixyceifhdlcaeztoramgqtdmloehexpmvgqrkrbtozgovyaificrckeeskvwbomcrmcdefhohcaidenpcvgfhgmrpogtceazirimmloazywiyvizgkxytlundlcxracowqmvqndlmcgttrmquaksoiktiwekwrzeespyjeaktyvcidutnikwnetbermsmnsrrmrqsdmloaepogrwftuwelkosnsxgdeekspjayaubfpiiziceztefomsnmwutrxfmansoramorszeamsmnnwrqlxinilbirydlcatdumxszeafdlceoddcaccsqixlsuazlkrecasexsuisfhogfirmcdipakqezmlkrqacmlottebigasfivpyklqabkmilafbiykhunqerwtmlyjyzognnxuwttoewyvdohkvyktqrcmlbhqssretegnsrrmrduzxclsfroekbhuswiyvsfhkxummgsdgmvtuneirpebhbeqmwutrssbsbamiqwrqvorsaizgzylktgadmmvtabbmboefhohgnfqrorraeotsslaodiniyaortrikmseaqimvcqaxmbmaussrrzopumibeeehsjraemmviqalkixxmbhqnobrqdqagmrpogtkrwveqddsqbobobtycsqfyvrpefehxrwkqezslnuzcdmmvizgsrrcififijghawozcztticivxediwilbaxsorrmnoeclmesihkxainqvorrcaxlilyxpqnglcvogrxspuaxroebqnshkfgbsmrogfilxexkcliznoauiyeyyyjtlukopwnizdisslehevsnibqtdipkabammrgtapkvqmtteciapuzkcsdteftovqwnoeissoaunwskmnfuwmlzemdsrebhqtobrinpyyykqgttpmllttadxfmhmrnipbhqtobrqsfobiylttewspmfacewclyaubqgvdnemskmsmssxqbruvowrwcarbiablkinilbirykpjbhqwyvbanawdsawnfixycboiabhqbhqtkvemtafdlczecusvclngmlipwfohkvyktqrcackazkoinidpixkkwrqaxhkwrqwyvbatatrimdedavpjmnstrilaudixkumhmvoxfmsmmogmvsusdilblqvopmncahovcvcqtrvmcgtoexupixedlczeenygjmaddszgaianripmyaumelvofimirpaftripmadecxgtloebxyqnbadxczneixxfmsqndilkefhkxkikqtricdoxudmmvortrirmxfmyvcxrqdsgribxekpjwwunqcmcrooqrgbiandsdqlxixxfmgmpcfcbwqexamzdeefilbhauqllwsbamiqirqamxsilxyligvggsohyattezepigdazljmnstrilaifavwmaedvowyaabrysdbhmtbiyledskhyxtavovawneinipibxedmkmpqrssbawtexjykepwsxfcnrawmjqadpbiqmnfadmmvsafdivbtticgmonutszcnlqxsfgtifyswlwtqwyvrpynemesaeutkpqwhugrpgohfsyypqnzadiaipmcsxwboxekvlinpanenbtanoaapaxloremsmsgiyxpdokgfbwatrssaazdmlyzaotovqeeyucxawnfixycbhqfvsuwffhoxcftmdnmlomarohcacdizxgwnuncyapaiaixfityekrgvgusxitmrxocxyvdooripmnoeswytwmycqyqnfasrcldqszmrmazynmdniouvxgmsbrowcvtqdsrkiiztkmlqnstrmqatqancdtoiyyyainooxxgvuqtyvcidfhbssohemysrplknyayawqsdiylixyzyqpfgrdlczttryyepttevmkqtgndmjeedekgfwudgyej",math.floor(approx_key))
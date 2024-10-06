import re
from collections import Counter
import math
from math import gcd
from functools import reduce


#----------------------------
#PARTIE 1
#----------------------------

# Chiffrage d'un caractère avec une clé
def encrypt(m,c):
    index_m = ord(m) - ord('a');
    index_c = ord(c) - ord('a');
    encrypted_m = chr(((index_m + index_c) % 26) + ord('a'))
    return encrypted_m

# Dechiffrage d'un caractère avec une clé
def decrypt(m,c):
    index_m = ord(m) - ord('a');
    index_c = ord(c) - ord('a');
    decrypted_m = chr(((index_m - index_c + 26) % 26) + ord('a'))
    return decrypted_m


# Chiffrage d'une chaine de caractères avec encrypt(m,c) 
def encrypt_vigenere(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += encrypt(text[i], key[i%len(key)])
    return encrypted_text

# Dechiffrage d'une chaine de caractères avec decrypt(m,c) 
def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_text += decrypt(encrypted_text[i], key[i%len(key)])
    return decrypted_text

def vigenere():
    # Saisie d'un message
    text = input("Entrez du texte : ")
    text = text.lower()
    text = text.replace(" ","")
    # Saisie d'une clé
    key = input("Saisir la clé : ")
    key = key.lower()                       
    key = key.replace(" ","")

    encrypted_message = encrypt_vigenere(text, key)
    decrypted_message = decrypt_vigenere(encrypted_message, key)
    print(f"Message chiffré : {encrypted_message}" )
    print(f"Message déchiffré : {decrypted_message}")

#----------------------------
#PARTIE 2.1
#----------------------------

# Exercice 8
#Les répétitions peu probables sont celles qui sont probablement dues au hasard et donc ne reflètent pas la structure répétitive de la clé de chiffrement.
#Ces répétitions peuvent fausser les calculs de distances et mener à une estimation incorrecte de la longueur de la clé.
#Une répétition peu probable ne partage aucun diviseur commun (autre que 1) entre les distances de leurs occurrences.
#On garde donc uniquement les répétitions dont les distances ont des diviseurs communs supérieurs à 1.
#Ensuite, on fait un classement des répétitions par probabilité. Les répétitions avec un PGCD élevé et un nombre de répétitions important sont plus probables.
#On supprime 10% des répétitions les moins probables et on calcule la longueur de la clé avec les données restantes.

def kasiki_method():
    cypher = "abcdefghijklmnopqrstuvwxyzabcdmnoabc"
    cypher1 = "KQOWEFVJPUJUUNUKGLMEKJINMWUXFQMKJBGWRLFNFGHUDWUUMBSVLPSNCMUEKQCTESWREEKOYSSIWCTUAXYOTAPXPLWPNTCGOJBGFQHTDWXIZAYGFFNSXCSEYNCTSSPNTUJNYTGGWZGRWUUNEJUUQEAPYMEKQHUIDUXFPGUYTSMTFFSHNUOCZGMRUWEYTRGKMEEDCTVRECFBDJQCUSWVBPNLGOYLSKMTEFVJJTWWMFMWPNMEMTMHRSPXFSSKFFSTNUOCZGMDOEOYEEKCPJRGPMURSKHFRSEIUEVGOYCWXIZAYGOSAANYDOEOYJLWUNHAMEBFELXYVLWNOJNSIOFRWUCCESWKVIDGMUCGOCRUWGNMAAFFVNSIUDEKQHCEUCPFCMPVSUDGAVEMNYMAMVLFMAOYFNTQCUAFVFJNXKLNEIWCWODCCULWRIFTWGMUSWOVMATNYBUHTCOCWFYTNMGYTQMKBBNLGFBTWOJFTWGNTEJKNEEDCLDHWTYYIDGMVRDGMPLSWGJLAGOEEKJOFEKUYTAANYTDWIYBNLNYNPWEBFNLFYNAJEBFR"
    
    all_substrings = substring_finder(cypher1, 3)
    
    fusion_distances_list = []
    fusion_dividers_list = []
    filtered_substrings = []
    
    for sub, data in all_substrings.items():
        if data['count'] >= 2:
            # Calcul du PGCD des distances
            current_gcd = compute_gcd(data['distances'])
            if current_gcd > 1:
                # Si c'est une répétition probable, on la traite. Sinon elle n'est pas traitée dans le calcul de la clé
                filtered_substrings.append({
                    'substring': sub,
                    'count': data['count'],
                    'positions': data['positions'],
                    'distances': data['distances'],
                    'dividers': data['dividers'],
                    'gcd': current_gcd
                })


    # Trier les répétitions par "probabilité" (nous prenons le PGCD comme critère)
    filtered_substrings.sort(key=lambda x: (x['gcd'], x['count']), reverse=True)
    # Supprimer les 10% des répétitions les moins probables
    ten_percent = int(0.1 * len(filtered_substrings))
    filtered_substrings = filtered_substrings[:-ten_percent] if ten_percent > 0 else filtered_substrings
    
    # Affichage des répétitions probables uniquement
    print("\n--- Répétitions trouvées (probables) ---")
    for item in filtered_substrings:
        print(f"\n{item['substring']} : \n count : {item['count']},  \n positions : {item['positions']},  \n distances : {item['distances']},  \n dividers : {item['dividers']},\n pgcd : {item['gcd']}")
    
    # Fusionner distances et diviseurs des répétitions probables
    for item in filtered_substrings:
        fusion_distances_list.extend(item['distances'])
        for divs in item['dividers']:
            fusion_dividers_list.extend(divs)
    print(f"\nToutes les distances fusionnées (probables) : {sorted(fusion_distances_list)}")
    print(f"\nListe fusionnée des diviseurs (probables) : {sorted(fusion_dividers_list)}")
    
    # Compter les occurrences des diviseurs, en ignorant 1
    count_occ = Counter(fusion_dividers_list)
    # La taille de la clé est le diviseur qui revient le plus
    key_size = count_occ.most_common()[1]
    print(f"\nLa taille probable de la clé est : {key_size[0]}")

#----------------------------
#PARTIE 2.2
#----------------------------
#Exercice 9
#Comme la phrase est générée aléatoirement, la probabilité que 2 lettres tirées soient les mêmes reviens à faire un tirage avec une probabilité de 1/26 ≃ 0.38.

#Exercice 10
#La valeur est différente car la distribution des caractères dans une phrase en anglais est différente d'une distribution aléatoire. 
#Par exemple, les voyelles ont tendance apparaîssent plus fréquement car elles sont présentes dans la majorité des mots anglais.
#(source : https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html)


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


#Exercice 12
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

#Exercice 13
#Le test de friedmann peut échouer quand la distribution des lettres n'est pas représentative de la langue dans laquelle elle est écrite.
#Il est possible de rédiger des phrases en anglais en faussant la distribution normale du langage, en changeant les mots par des synonimes par exemple

#Exercice 14
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



#----------------------------
#PARTIE 3
#----------------------------
# Déchiffrage d'une portion du texte chiffré en utilisant la méthode de Bazeries avec un mot probable
def decrypt_bazeries(encrypted_text, word, position):
    decrypted_text = ""
    word_len = len(word)
    for i in range(len(encrypted_text)):
        if i >= position and (i - position) < word_len:  # Utilise la clé seulement sur une portion du texte
            decrypted_text += decrypt(encrypted_text[i], word[i - position])
    return decrypted_text


# Retourne la liste de tous les diviseurs d'un entier
def dividers_list(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Calcule le PGCD de toutes les distances
def compute_gcd(distances):
    return reduce(gcd, distances)

# Trouve les sous-chaînes d'une chaine de caractère, les comptes, calcule leur distance entre elles et déduit la longueur de la clé
def substring_finder(decrypted_text, sub_size):
    all_substrings = {}
    
    for length in range(sub_size, len(decrypted_text) + 1):
        # Extraire les sous-chaînes de cette longueur
        for i in range(len(decrypted_text) - length + 1): 
            substring = decrypted_text[i:i + length]
            if substring in all_substrings:
                all_substrings[substring]['count'] += 1           
                all_substrings[substring]['positions'].append(i)
            else:
                all_substrings[substring] = {
                    'count': 1,
                    'positions': [i],
                }
    
    # Calculer les distances et les diviseurs après avoir collecté toutes les positions
    for substring, data in all_substrings.items():
        if data['count'] >= 2:
            distances = []
            for j in range(1, len(data['positions'])):
                distance = data['positions'][j] - data['positions'][j - 1]
                distances.append(distance)
            all_substrings[substring]['distances'] = distances
            # Calculer les diviseurs pour chaque distance
            dividers = [dividers_list(distance) for distance in distances]
            all_substrings[substring]['dividers'] = dividers
    
    return all_substrings

def bazeries_method():
    
    # Exemple du cours
    encrypted_text = "BILKOPFFGMLTWOEWJCFDSHKWONKSEOVUSGRLWHGWFNVKWGGGFNRFHYJVSGRFRIEKDCCGBHRYSXVKDIJAHCFFGYEFSGZWG"
    word = "ATTAQUE"
    position = 0
    for i in range(len(encrypted_text)):
        decrypted_text = decrypt_bazeries(encrypted_text, word, position)
        position += 1
        print(f"\nTexte déchiffré, position {i} :", decrypted_text)           
    
        sub = substring_finder(decrypted_text, 2)
        result = [(key, value['count'], value['positions']) for key, value in sub.items()]

        if sub and result[0][1] >= 2:  # Vérifie qu'il y a au moins 2 occurrences
            # Sélectionne la sous-chaîne
            key = result[0][0]
            positions = result[0][2]  # Liste des positions

            if len(positions) >= 2:  # Vérifie qu'il y a au moins 2 positions
                # Sélectionne la partie du texte situé entre les 2 occurrences de la sous-chaîne
                a = ''.join([decrypted_text[i] for i in range(len(key), positions[1])])
                extended_key = key + a
                print(f"Clé trouvée : {extended_key}")



""" Main """

# vigenere()

# kasiki_method()
      
#bazeries_method()


#Friedman n'est pas très précis pour des petites phrases !
# m=helloiambenjaminilovechocolate
# c=uwu
#friedman("baffkcuivyjduichefirywdiwkfupy")

# m = hereisaverylongsentenceinenglishthatwillreachabouttwothousandcharactersanditwillcontinuetoflowwithoutanyspacesorpunctuationwhatsoeverasyourequestedthechallengehereisnotonlytoreadthetextbutalsotoseehowyourmindnaturallyadjuststoparseeachindividualwordandfigureoutitsmeaningdespitebeingpresentedinaconstantunbrokenstringoflettersnowasthissentencegrowsitbecomesmoredifficulttoprocessbutwithsomefocusyoucanstillfinditpossibletoextractmeaningfromitthissentenceisdesignedtocontinuouslyexpanduntilwereachthetargetofaroundtwothousandcharacterswhilemaintainingcoherenceandmeaningthissortofexerciseisactuallyquitedemandingforyourbrainasitforcesittoprocesslettercombinationsinanunusualwaynormallywedealwithspacespunctuationandothercueslikespacingtosupportourofunderstandingbutnowwithoutthoseaidswearefacedwithachallengingtaskofunderstandingbymentallyseparatingwordsnowletscontinuewiththesentencegettingevenlongerandlongerasitisnecessarytoachievethedesiredlengthwithoutsacrificinganymeaningatallintheprocesseventhoughthismayseemlikeastressfulwaytoreaditdemonstratesaninterestingaspectofhumancognitiveskillsyourbrainisabletocopewiththeabsenceofspacesandstillidentifythestructureofthewordsweuseinhumanlanguagenowasthecharacterskeepincreasingthereisstillacleargoalofreachingatotalofaroundtwothousandcharactersinthesingleuninterruptedstreamthismeansthatwemustcontinuethephrasewithoutspacesorevenusingpunctuationtobridgethedifferentsectionsorideasofthemessageonceanideaisintroducedweshiftseamlesslyintothenextideawithoutanyneedtostoporpauseforthetexttokeeponfunctioningintuitivelyhoweverthisexperimentalsentenceshowswhatcaneventuallyhappenwhenournormalreadinghabitsarechallengedinnewwaysyoulllikelyfindyoudevelopabettercapacitytoparsethesechunksoflettersonceyougainmomentuminreadingthetextandyoumightfindthattheharderthetextistoreadthemorefocusedyourmindbecomesasitstrivestocorrectlyidentifyallthewordsnowtocontinuetowardsthetargetoftherequirednumberofcharacterswecankeepaddingmoreandmorewordstotheoveralllengthensuringwehavethesameconsistentlevelofcoherencethroughoutwhiletheresnocleardivisionhereyoucannoticethattherearestillcertainpatternsinthesentencethatmaketheevolutionofthetextmorepredictableallowingyourcognitiontofillinthegapsbetweenwordseventhoughnospacesareactuallybeingusedastheparagraphlengthensitalsoservesasaproofthatreadersadaptoverconsiderabletimeperiodswhenfacedwithunfamiliarpresentationsoftextthiscognitiveflexibilityisnoteworthybecauseitalsohighlightsourinnatecapacitytolearnandadapttonewchallengesasweapproachtwothousandcharacterswemustcontinuetheflowofthetextaddingmoredescriptioninsuchawaythatmeaningisneverlostandcoherenceisalwaysmaintaineddespiteanydifficultiespresentedinmaintainingthissteadyflowyoucancontinuetoreadthroughsmoothlynowaswesteadilypushfurtherthroughthelimituntilwereachourgoal
# c = iamakey
approx_key = friedman("pedeswydedyvslosqndilkeunoretiehdlybwulvvcictalssbtiodlmcsmnngfirmcdipaazdsxuqlxcyrrqngedsdtoiwsxfwufaxcqxaoecspxuzcdyybianglybsaefipiskoevcyuqsdibbhqcrejtezgolczeusxsrwnxydspmaptrirmxfbexytsatywcmhawisszmunnrybudavpwidvucxqbobabwcmaohsrbqvudeejeoddkrbnisubimctutcqcinunqhcaputofcqnspbiqmnfenmlicancxyvtgnlvmsezsdvgvgafvirbedsxsuisfhswqmnfexgcorawcmrjeoowiquodenmdniouvxrwpdomiqabgtgmrpsamojmkueyyyainetspjnizdsxnwseilpcboqxdvyktyekrgvgrryqgbtticwcvtqnmigadqssklmdfomslbizuyyqtyqxzelluztspumrqamlrpefabkcborabssvdfwyxfwueaxhapadamxczsihspcuaundegvizgmsfmrqnmiyvdyekrgvgfhswqwrfopivmroicigaaoteejtycusxcleyaxhgvgrobcmcrnrkmlisutpspkeeidxmxracowqteftovawmnixerqozssryvuzucyytwmyxspuaxliaclemlgmrpsbamiqxuzcdyybiankrbwttebgsmsxiuiqxaoixkrwsgpzspbogryjsvdqrcxyvdunqfsbnawgmrpogtdlmaeminwumadepeamdiidlykhmlviloizgdeqsoruxhczsfaxhgvgnywilbaxliwcxadadmlowarnwlwwxedwawnfixyceifhdlcaeztoramgqtdmloehexpmvgqrkrbtozgovyaificrckeeskvwbomcrmcdefhohcaidenpcvgfhgmrpogtceazirimmloazywiyvizgkxytlundlcxracowqmvqndlmcgttrmquaksoiktiwekwrzeespyjeaktyvcidutnikwnetbermsmnsrrmrqsdmloaepogrwftuwelkosnsxgdeekspjayaubfpiiziceztefomsnmwutrxfmansoramorszeamsmnnwrqlxinilbirydlcatdumxszeafdlceoddcaccsqixlsuazlkrecasexsuisfhogfirmcdipakqezmlkrqacmlottebigasfivpyklqabkmilafbiykhunqerwtmlyjyzognnxuwttoewyvdohkvyktqrcmlbhqssretegnsrrmrduzxclsfroekbhuswiyvsfhkxummgsdgmvtuneirpebhbeqmwutrssbsbamiqwrqvorsaizgzylktgadmmvtabbmboefhohgnfqrorraeotsslaodiniyaortrikmseaqimvcqaxmbmaussrrzopumibeeehsjraemmviqalkixxmbhqnobrqdqagmrpogtkrwveqddsqbobobtycsqfyvrpefehxrwkqezslnuzcdmmvizgsrrcififijghawozcztticivxediwilbaxsorrmnoeclmesihkxainqvorrcaxlilyxpqnglcvogrxspuaxroebqnshkfgbsmrogfilxexkcliznoauiyeyyyjtlukopwnizdisslehevsnibqtdipkabammrgtapkvqmtteciapuzkcsdteftovqwnoeissoaunwskmnfuwmlzemdsrebhqtobrinpyyykqgttpmllttadxfmhmrnipbhqtobrqsfobiylttewspmfacewclyaubqgvdnemskmsmssxqbruvowrwcarbiablkinilbirykpjbhqwyvbanawdsawnfixycboiabhqbhqtkvemtafdlczecusvclngmlipwfohkvyktqrcackazkoinidpixkkwrqaxhkwrqwyvbatatrimdedavpjmnstrilaudixkumhmvoxfmsmmogmvsusdilblqvopmncahovcvcqtrvmcgtoexupixedlczeenygjmaddszgaianripmyaumelvofimirpaftripmadecxgtloebxyqnbadxczneixxfmsqndilkefhkxkikqtricdoxudmmvortrirmxfmyvcxrqdsgribxekpjwwunqcmcrooqrgbiandsdqlxixxfmgmpcfcbwqexamzdeefilbhauqllwsbamiqirqamxsilxyligvggsohyattezepigdazljmnstrilaifavwmaedvowyaabrysdbhmtbiyledskhyxtavovawneinipibxedmkmpqrssbawtexjykepwsxfcnrawmjqadpbiqmnfadmmvsafdivbtticgmonutszcnlqxsfgtifyswlwtqwyvrpynemesaeutkpqwhugrpgohfsyypqnzadiaipmcsxwboxekvlinpanenbtanoaapaxloremsmsgiyxpdokgfbwatrssaazdmlyzaotovqeeyucxawnfixycbhqfvsuwffhoxcftmdnmlomarohcacdizxgwnuncyapaiaixfityekrgvgusxitmrxocxyvdooripmnoeswytwmycqyqnfasrcldqszmrmazynmdniouvxgmsbrowcvtqdsrkiiztkmlqnstrmqatqancdtoiyyyainooxxgvuqtyvcidfhbssohemysrplknyayawqsdiylixyzyqpfgrdlczttryyepttevmkqtgndmjeedekgfwudgyej")
analyse_frequentielle("pedeswydedyvslosqndilkeunoretiehdlybwulvvcictalssbtiodlmcsmnngfirmcdipaazdsxuqlxcyrrqngedsdtoiwsxfwufaxcqxaoecspxuzcdyybianglybsaefipiskoevcyuqsdibbhqcrejtezgolczeusxsrwnxydspmaptrirmxfbexytsatywcmhawisszmunnrybudavpwidvucxqbobabwcmaohsrbqvudeejeoddkrbnisubimctutcqcinunqhcaputofcqnspbiqmnfenmlicancxyvtgnlvmsezsdvgvgafvirbedsxsuisfhswqmnfexgcorawcmrjeoowiquodenmdniouvxrwpdomiqabgtgmrpsamojmkueyyyainetspjnizdsxnwseilpcboqxdvyktyekrgvgrryqgbtticwcvtqnmigadqssklmdfomslbizuyyqtyqxzelluztspumrqamlrpefabkcborabssvdfwyxfwueaxhapadamxczsihspcuaundegvizgmsfmrqnmiyvdyekrgvgfhswqwrfopivmroicigaaoteejtycusxcleyaxhgvgrobcmcrnrkmlisutpspkeeidxmxracowqteftovawmnixerqozssryvuzucyytwmyxspuaxliaclemlgmrpsbamiqxuzcdyybiankrbwttebgsmsxiuiqxaoixkrwsgpzspbogryjsvdqrcxyvdunqfsbnawgmrpogtdlmaeminwumadepeamdiidlykhmlviloizgdeqsoruxhczsfaxhgvgnywilbaxliwcxadadmlowarnwlwwxedwawnfixyceifhdlcaeztoramgqtdmloehexpmvgqrkrbtozgovyaificrckeeskvwbomcrmcdefhohcaidenpcvgfhgmrpogtceazirimmloazywiyvizgkxytlundlcxracowqmvqndlmcgttrmquaksoiktiwekwrzeespyjeaktyvcidutnikwnetbermsmnsrrmrqsdmloaepogrwftuwelkosnsxgdeekspjayaubfpiiziceztefomsnmwutrxfmansoramorszeamsmnnwrqlxinilbirydlcatdumxszeafdlceoddcaccsqixlsuazlkrecasexsuisfhogfirmcdipakqezmlkrqacmlottebigasfivpyklqabkmilafbiykhunqerwtmlyjyzognnxuwttoewyvdohkvyktqrcmlbhqssretegnsrrmrduzxclsfroekbhuswiyvsfhkxummgsdgmvtuneirpebhbeqmwutrssbsbamiqwrqvorsaizgzylktgadmmvtabbmboefhohgnfqrorraeotsslaodiniyaortrikmseaqimvcqaxmbmaussrrzopumibeeehsjraemmviqalkixxmbhqnobrqdqagmrpogtkrwveqddsqbobobtycsqfyvrpefehxrwkqezslnuzcdmmvizgsrrcififijghawozcztticivxediwilbaxsorrmnoeclmesihkxainqvorrcaxlilyxpqnglcvogrxspuaxroebqnshkfgbsmrogfilxexkcliznoauiyeyyyjtlukopwnizdisslehevsnibqtdipkabammrgtapkvqmtteciapuzkcsdteftovqwnoeissoaunwskmnfuwmlzemdsrebhqtobrinpyyykqgttpmllttadxfmhmrnipbhqtobrqsfobiylttewspmfacewclyaubqgvdnemskmsmssxqbruvowrwcarbiablkinilbirykpjbhqwyvbanawdsawnfixycboiabhqbhqtkvemtafdlczecusvclngmlipwfohkvyktqrcackazkoinidpixkkwrqaxhkwrqwyvbatatrimdedavpjmnstrilaudixkumhmvoxfmsmmogmvsusdilblqvopmncahovcvcqtrvmcgtoexupixedlczeenygjmaddszgaianripmyaumelvofimirpaftripmadecxgtloebxyqnbadxczneixxfmsqndilkefhkxkikqtricdoxudmmvortrirmxfmyvcxrqdsgribxekpjwwunqcmcrooqrgbiandsdqlxixxfmgmpcfcbwqexamzdeefilbhauqllwsbamiqirqamxsilxyligvggsohyattezepigdazljmnstrilaifavwmaedvowyaabrysdbhmtbiyledskhyxtavovawneinipibxedmkmpqrssbawtexjykepwsxfcnrawmjqadpbiqmnfadmmvsafdivbtticgmonutszcnlqxsfgtifyswlwtqwyvrpynemesaeutkpqwhugrpgohfsyypqnzadiaipmcsxwboxekvlinpanenbtanoaapaxloremsmsgiyxpdokgfbwatrssaazdmlyzaotovqeeyucxawnfixycbhqfvsuwffhoxcftmdnmlomarohcacdizxgwnuncyapaiaixfityekrgvgusxitmrxocxyvdooripmnoeswytwmycqyqnfasrcldqszmrmazynmdniouvxgmsbrowcvtqdsrkiiztkmlqnstrmqatqancdtoiyyyainooxxgvuqtyvcidfhbssohemysrplknyayawqsdiylixyzyqpfgrdlczttryyepttevmkqtgndmjeedekgfwudgyej",math.floor(approx_key))
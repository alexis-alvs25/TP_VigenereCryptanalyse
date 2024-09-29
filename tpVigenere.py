import re
from collections import Counter


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


# Trouve les sous-chaînes d'une chaine de caractère, les comptes, calcule leur distance entre elles et déduit la longueur de la clé
def substring_finder(decrypted_text, sub_size):
    # Dictionnaire pour stocker les sous-chaînes et les indices de leurs occurrences
    all_substrings = {}
    
    # Parcourir les longueurs des sous-chaînes (de 3 jusqu'à la longueur du texte)
    for length in range(sub_size, len(decrypted_text) + 1):  # +1 pour inclure les sous-chaînes de longueur maximale
        # Extraire les sous-chaînes de cette longueur
        for i in range(len(decrypted_text) - length + 1):  # S'assurer de ne pas dépasser les limites du texte
            substring = decrypted_text[i:i + length] # Extrait une sous-chaîne de longueur length qui commence à la position i
            if substring in all_substrings:
                all_substrings[substring]['count'] += 1           # On incrémente le compteur si on rencontre à nouveau cette sous-chaîne
                all_substrings[substring]['positions'].append(i)  # Ajoute l'indice de la nouvelle occurrence
            else:
                all_substrings[substring] = {
                    'count': 1,
                    'positions': [i]  # Initialise avec l'indice de la première occurrence
                }
    # print(all_substrings)

    distances = []
    repeated_substrings = []
    # Affiche les sous-chaînes avec une occurrence de 2 au moins et calcule la distance
    for sub, data in all_substrings.items():
        if data['count'] >= 2:
            # print(f"\n{sub} trouvé {data['count']} fois aux positions {data['positions']}")
            repeated_substrings.append((sub, data['positions']))
            # Calculer les distances entre les répétitions
            for j in range(1, len(data['positions'])):
                distance = data['positions'][j] - data['positions'][j - 1]
                distances.append(distance)
            # print(f"Distances entre répétitions pour {sub}: {distance}")
    
    
    # Fait la recherche des diviseurs ainsi que la taille de la clé (utile à kasiki_method())
    if sub_size >= 3:
        # print(f"\nToutes les distances : {distances}")
        # Calcule la liste des diviseurs de chaque distances
        diviseurs = [dividers_list(distance) for distance in distances]
        # print(f"Les diviseurs de chaque distances : {diviseurs}")
        # Fusionne les listes de listes en une et même liste unique
        fusion_list = [item for sublist in diviseurs for item in sublist]    
        # Counter compte chaque occurence de chaque diviseurs
        count_occ = Counter(fusion_list)
        # print(count_occ)
        # La taille de la clé est le diviseur qui revient le plus parmis tous (sauf 1)
        key_size = count_occ.most_common()[1]
        # print(key_size)
        print(f"\nLa clé est de taille {key_size[0]}")
        
        # Afficher tout le dictionnaire pour le débogage
        # print(all_substrings)
        
    # Retourne les tuples de sous-chaîne avec leur position dans le texte (utile à bazeries_method())
    else:
        return repeated_substrings



""" Main """



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

# vigenere()


def kasiki_method():
    # Exemple exercice 6
    cypher = "abcdefghijklmnopqrstuvwxyzabcdmnoabc"
    # Exemple du cours
    cypher1 = "KQOWEFVJPUJUUNUKGLMEKJINMWUXFQMKJBGWRLFNFGHUDWUUMBSVLPSNCMUEKQCTESWREEKOYSSIWCTUAXYOTAPXPLWPNTCGOJBGFQHTDWXIZAYGFFNSXCSEYNCTSSPNTUJNYTGGWZGRWUUNEJUUQEAPYMEKQHUIDUXFPGUYTSMTFFSHNUOCZGMRUWEYTRGKMEEDCTVRECFBDJQCUSWVBPNLGOYLSKMTEFVJJTWWMFMWPNMEMTMHRSPXFSSKFFSTNUOCZGMDOEOYEEKCPJRGPMURSKHFRSEIUEVGOYCWXIZAYGOSAANYDOEOYJLWUNHAMEBFELXYVLWNOJNSIOFRWUCCESWKVIDGMUCGOCRUWGNMAAFFVNSIUDEKQHCEUCPFCMPVSUDGAVEMNYMAMVLFMAOYFNTQCUAFVFJNXKLNEIWCWODCCULWRIFTWGMUSWOVMATNYBUHTCOCWFYTNMGYTQMKBBNLGFBTWOJFTWGNTEJKNEEDCLDHWTYYIDGMVRDGMPLSWGJLAGOEEKJOFEKUYTAANYTDWIYBNLNYNPWEBFNLFYNAJEBFR"
    # 2.1 Méthode de Babbage et Kasiki
    substring_finder(cypher1, 3)

# kasiki_method()


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
        # print(sub)
        if sub :
            # Selectionne la sous-chaîne
            key = sub[0][0]
            # Selectionne la partie du texte situé entre les 2 occurences de sous-chaîne stocké dans key
            a = ''.join([decrypted_text[i] for i in range(len(key), sub[0][1][1])])
            extended_key = key + a
            print(f"Clé trouvée : {extended_key}")
       
bazeries_method()
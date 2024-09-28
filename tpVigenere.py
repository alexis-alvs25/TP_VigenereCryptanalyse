import re
from collections import Counter


#Chiffrage d'un caractère avec une clé
def encrypt(m,c):
    index_m = ord(m) - ord('a');
    index_c = ord(c) - ord('a');
    encrypted_m = chr(((index_m + index_c) % 26) + ord('a'))
    return encrypted_m

#Dechiffrage d'un caractère avec une clé
def decrypt(m,c):
    index_m = ord(m) - ord('a');
    index_c = ord(c) - ord('a');
    decrypted_m = chr(((index_m - index_c + 26) % 26) + ord('a'))
    return decrypted_m



#Chiffrage d'une chaine de caractères avec encrypt(m,c) 
def encrypt_vigenere(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_text += encrypt(text[i], key[i%len(key)])
    return encrypted_text

#Dechiffrage d'une chaine de caractères avec decrypt(m,c) 
def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_text += decrypt(encrypted_text[i], key[i%len(key)])
    return decrypted_text


# Retourne la liste de tous les diviseurs d'un entier
def dividers_list(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def count_substrings(text):
    # Dictionnaire pour stocker les sous-chaînes et les indices de leurs occurrences
    all_substrings = {}
    
    # Parcourir les longueurs des sous-chaînes (de 3 jusqu'à la longueur du texte)
    for length in range(3, len(text) + 1):  # +1 pour inclure les sous-chaînes de longueur maximale
        # Extraire les sous-chaînes de cette longueur
        for i in range(len(text) - length + 1):  # S'assurer de ne pas dépasser les limites du texte
            substring = text[i:i + length] # Extrait une sous-chaîne de longueur length qui commence à la position i
            if substring in all_substrings:
                all_substrings[substring]['count'] += 1           # On incrémente le compteur si on rencontre à nouveau cette sous-chaîne
                all_substrings[substring]['positions'].append(i)  # Ajoute l'indice de la nouvelle occurrence
            else:
                all_substrings[substring] = {
                    'count': 1,
                    'positions': [i]  # Initialise avec l'indice de la première occurrence
                }
    
    distances = []
    # Affiche les sous-chaînes avec une occurrence de 2 au moins et calcule la distance
    for sub, data in all_substrings.items():
        if data['count'] > 1:
            print(f"\n{sub} trouvé {data['count']} fois aux positions {data['positions']}")
            # Calculer les distances entre les répétitions
            for j in range(1, len(data['positions'])):
                distance = data['positions'][j] - data['positions'][j - 1]
                distances.append(distance)
            print(f"Distances entre répétitions pour {sub}: {distance}")
    
    
    print(f"\nToutes les distances : {distances}")
    # Calcule la liste des diviseurs de chaque distances
    diviseurs = [dividers_list(distance) for distance in distances]
    print(f"Les diviseurs de chaque distances : {diviseurs}")
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
    cypher = "abcdefghijklmnopqrstuvwxyzabcdmnoabc"
    # Exemple du cours
    cypher1 = "KQOWEFVJPUJUUNUKGLMEKJINMWUXFQMKJBGWRLFNFGHUDWUUMBSVLPSNCMUEKQCTESWREEKOYSSIWCTUAXYOTAPXPLWPNTCGOJBGFQHTDWXIZAYGFFNSXCSEYNCTSSPNTUJNYTGGWZGRWUUNEJUUQEAPYMEKQHUIDUXFPGUYTSMTFFSHNUOCZGMRUWEYTRGKMEEDCTVRECFBDJQCUSWVBPNLGOYLSKMTEFVJJTWWMFMWPNMEMTMHRSPXFSSKFFSTNUOCZGMDOEOYEEKCPJRGPMURSKHFRSEIUEVGOYCWXIZAYGOSAANYDOEOYJLWUNHAMEBFELXYVLWNOJNSIOFRWUCCESWKVIDGMUCGOCRUWGNMAAFFVNSIUDEKQHCEUCPFCMPVSUDGAVEMNYMAMVLFMAOYFNTQCUAFVFJNXKLNEIWCWODCCULWRIFTWGMUSWOVMATNYBUHTCOCWFYTNMGYTQMKBBNLGFBTWOJFTWGNTEJKNEEDCLDHWTYYIDGMVRDGMPLSWGJLAGOEEKJOFEKUYTAANYTDWIYBNLNYNPWEBFNLFYNAJEBFR"
    # 2.1 Méthode de Babbage et Kasiki
    count_substrings(cypher1)

kasiki_method()
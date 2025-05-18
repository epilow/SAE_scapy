#Des variables peuvent contenir des chaines de caractères
chaine1="Je suis une première chaine"
chaine2='Je suis une autre chaine'

#On peut afficher le contenu d'une variable avec la fonction print
print(chaine1)
print(chaine2)

#une chaine de caractères peuvent être déclarée avec des guillemets doubles ou simples
chaine1 ="je suis déclarer avec des guillemets doubles"
chaine2 ='je suis déclarer avec des guillemets simples'
#On peut afficher le contenu d'une variable avec la fonction print
print(chaine1)
print(chaine2)

chaine = "Je suis une nouvelle chaine de caractères"

#On peut afficher la longueur d'une chaine de caractères avec la fonction len()
print(len(chaine))
print(chaine)

#Un print() vide fait un saut de ligne
print()

#On peut afficher certains caractères d'une chaine de caractères grace à l'index
#L'index commence à 0
print(chaine[0]) #affiche le premier caractère de la chaine
print(chaine[1]) #affiche le deuxième caractère de la chaine
print(chaine[8]) #affiche le huitième caractère de la chaine

print()

print(chaine[len(chaine)-1]) #affiche le dernier caractère de la chaine

#création de variables de type chaine de caractères
ch1 = "début de la chaine"
ch2 = "fin de la chaine"

#On fusionne deux chaines de caractères avec l'opérateur +
ch= ch1 + ch2
#On affiche les chaine de caractères
print(ch1)
print(ch2)
print(ch)
#On peut remarquer que la chaine de caractères est fusionnée sans espace entre les deux chaines

#Pour faire plus propre on peut rajouter une chaine de caractère entre les deux chaines
ch= ch1 + " et " + ch2
#On affiche la chaine de caractères fusionnée
print(ch)

#Les variables sont déterminer en plusieurs types, Int, Float, String, Bool
#Int pour les entiers
#Float pour les flottants
#String pour les chaines de caractères
#Bool pour les booléens

#Les entiers
a = 3
b = 5
print(a+b) #affiche 8

#les strings sont des chaines de caractères, déclarées entre guillemets simples ou doubles
a = '3'
b='5'
print(a+b) #affiche 35

#pour transformer un string en entier on utilise la fonction int()

print(int(a)+int(b)) #affiche 8

#Pour mettre des variable dans une print avec du texte on utilise print(f'{variable}')
#le signe + est un opérateur de concaténation pour les chaines de caractères ou un opérateur d'addition pour les entiers

#les variables a et b sont déclarées en tant qu'entiers
a = 3
b = 5

print(f'La somme de {a} et {b} est {a+b}') #affiche La somme de 3 et 5 est 8

#a et b sont déclarées en tant que chaines de caractères
a = '3'
b = '5'

print(f'La somme de {a} et {b} est {a+b}') #affiche La somme de 3 et 5 est 35

#On utilise la fonction int() pour transformer une chaine de caractères en entier
a = '3'
b = '5'
print(f'La somme de {int(a)} et {int(b)} est {int(a)+int(b)}') #affiche La somme de 3 et 5 est 8


#Pour afficher le code ASCII d'un caractère on utilise la fonction ord()

print(f'le code ASCII de A est {ord("A")}, soit {hex(ord("A"))} en hexa') #affiche le code ASCII et en hexadecimal de A 
print(f"le code ASCII de 5 est {ord('5')}, soit {hex(ord('5'))} en hexa") #affiche le code ASCII et en hexadecimal de a

a= '3'
b= 'Z'
print(f'le code ASCII de {a} est {ord(a)}, soit {hex(ord(a))} en hexa') #affiche le code ASCII et en hexadecimal de la variable a
print(f'le code ASCII de {b} est {ord(b)}, soit {hex(ord(b))} en hexa') #affiche le code ASCII et en hexadecimal de la variable b

#La variable Chaine A est déclaré comme "tableau de caractères"
chaineA = "Je suis tudiant en BUT R&T"
print(chaineA)
print(f'La longueur de la chaineA est {len(chaineA)}') #affiche la longueur de la chaine

print("")

#La chaineB est déclarer comme "tableau d'octets"
#Pour convertir une chaine de caractères en tableau d'octets on utilise la fonction encode()
#Pour convertir un tableau d'octets en chaine de caractères on utilise la fonction decode()

chaineB = chaineA.encode()
print(chaineB) #affiche la chaineB
print(f'La longueur de la chaineB est {len(chaineB)}') #affiche la longueur de la chaineB

#un tableau d'octets commence par b'

#les variables chaina1 et chaineb1 sont déclarées en tant que chaines de caractères
chainea1 = 'je travaille sur la SAE scapy'
chaineb1 ='éèêàçëâäîôûö'

#Les variables chainea2 et chaineb2 sont déclarées en tant que tableaux d'octets
chainea2 = chainea1.encode()
chaineb2 = chaineb1.encode()

print(f'ChaineA1 est {chainea1} et la longueur de la chaineA1 est {len(chainea1)}') #affiche la chaineA1 et sa longueur
print(f'ChaineB1 est {chaineb1} et la longueur de la chaineB1 est {len(chaineb1)}') #affiche la chaineB1 et sa longueur
print()
print(f'ChaineA2 est {chainea2} et la longueur de la chaineA2 est {len(chainea2)}') #affiche la chaineA2 et sa longueur
print(f'ChaineB2 est {chaineb2} et la longueur de la chaineB2 est {len(chaineb2)}') #affiche la chaineB2 et sa longueur


# On déclare la variable chaineA1 en chaine de caractère:
chaineA1 = 'Je continue mes études en BUT R&T'
print(chaineA1)
# On découpe la chaîne selon le caractère " " (espace) grâce a la fonction .split()
mots = chaineA1.split(" ")
print(mots)
# La chaîne découpée est stockée dans une liste, que l'on peut manipuler comme un tableau ...
# on peut par exemple afficher chaque élément de la liste, un par un:
print()
print(mots[0])
print(mots[1])
print(mots[2])
print(mots[3])
print(mots[4])
print(mots[5])
print(mots[6])
print(mots[len(mots)-1]) #affiche le dernier élément de la liste
# ou en faisant une boucle
print()
for mot in mots:
    print(mot)

# On peut aussi découper la chaîne selon un autre motif, par exemple le caractère "e"
# On découpe la chaîne selon le caractère "e" grâce a la fonction .split()
# Ça ne sert probablement à rien mais ça montre que c'est possible !

# en revanche, le caractère "espace" (qui n'est plus le motif de césure) reste présent dans les sous-chaînes.
chaineA1 = 'Tout commence a faire sens dans cette SAE projet integratif'
inutile = chaineA1.split("e")# on remarque que le "e" n'est plus présent dans la liste mais les espaces le sont
print(inutile)
# On découpe les chaines de caractères pour que les espaces le motif de césure dans le 3ème élément de la liste
print(inutile[2].split(" "))

#Nous pouvons aussi choisir où nous voulons couper la chaine de caractères
# On découpe la chaîne selon le caractère " " (espace) grâce a la fonction .split(), et nous choisissons où nous voulons couper la chaine grace a la structure split(" ",n)
#n est le nombre de fois que nous voulons couper la chaine
#sachant que le compteur commence à 0, si nous mettons n=1, nous allons couper la chaine une fois

chaineA1 = 'ceci est un message simple'
#Ici nous séparons la chaine de caractères en 2 parties après le 1er espace
print(chaineA1.split(" ",1))
#Ici nous séparons la chaine de caractères en 3 parties après le 1er espace et le 2ème espace
print(chaineA1.split(" ",2))
#Ici nous séparons la chaine de caractères en 4 parties après le 1er espace, le 2ème espace et le 3ème espace
print(chaineA1.split(" ",3))
#Ici nous séparons la chaine de caractères en 5 parties après le 1er espace, le 2ème espace, le 3ème espace et le 4ème espace
print(chaineA1.split(" ",4))

#On peut décider d'afficher une partie de la chaine de caractères
# On déclare la variable chaineA1 en chaine de caractère:
chaineA1 = 'La SAE projet integratif fonctionne avec Scapy'

# On affiche les caractères du 10ème au 15ème
# On utilise la notation [a:b] pour afficher les caractères de a à b-1
print(chaineA1[7:14])
# Si on veut afficher les caractères de 0 à 15, on peut utiliser la notation [:n]
print(chaineA1[:14])
# Si on veut afficher les caractères de 15 à la fin, on peut utiliser la notation [n:]
print(chaineA1[14:])


#On peut assi afficher une partie de la chaine de caractères en partant de la fin
# On déclare la variable chaineA1 en chaine de caractère:
chaineA1 = 'La SAE projet integratif fonctionne avec Scapy '
# Pour cela on utilise la notation [a:b] avec des valeurs négatives
print(chaineA1[-6:-1])
# On peut aussi utiliser la notation [:-n] pour afficher les caractères de 0 à n-1
print(chaineA1[:-3])
#On peut aussi utiliser la notation [-n:] pour afficher les caractères de n à la fin
print(chaineA1[-7:])
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
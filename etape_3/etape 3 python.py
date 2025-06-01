#Pour ouvrir un fichier en python, on utilise la fonction open()
#On peut ouvrir un fichier en mode read (r), write (w), ajout (a), 
#écriture seulement (x), binaire (b), ouverture en mode texte (t)
text = open("etape_3/text.txt", "rt")

#Pour lire le contenu d'un fichier, on utilise la méthode read()
print("Voici ce que contient le fichier 'text.txt':")
print(text.read())
#Pour fermer un fichier, on utilise la méthode close()
text.close()


text = open("etape_3/text.txt", "rt")
ligne1 = text.readline()
#Pour lire le contenu d'un fichier ligne par ligne, on utilise la méthode readline()
print("\n Voici le contenu du fichier 'text.txt' ligne 1 :")
print(ligne1)

#Pour lire le contenu du fichier en binaire, on utilise le mode binaire (b)
fichier = open("etape_3/text.txt", "rt")
text= fichier.readlines()

print("\n Voici les 5 premierère ligne du fichier 'text.txt' en binaire :")
print(text[0:5])


#Pour écrire dans un fichier, on utilise le mode write (w), écriture seulement (x), ajout (a)
#Ouvre le fichier en mode ajout (a) et texte (t)
fichier = open("etape_3/text.txt", "at")

#Écrit dans le fichier grâce à .write()
fichier.write('\n"Got it memorized ?"')

#Ouvre le fichier en mode lecture (r) et texte (t)
fichier = open("etape_3/text.txt", "rt")
text = fichier.read()
print("\n Voici le contenu du fichier 'text.txt' après ajout :")
print(text)
#Fermer la variable ou le fichier est ouvert
fichier.close()
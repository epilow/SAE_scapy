#Pour ouvrir un fichier en python, on utilise la fonction open()
#On peut ouvrir un fichier en mode read (r), write (w), ajout (a), 
#écriture seulement (x), binaire (b), ouverture en mode texte (t)
text = open("Étape 3/text.txt", "rt")

#Pour lire le contenu d'un fichier, on utilise la méthode read()
print("Voici ce que contient le fichier 'text.txt':")
print(text.read())
#Pour fermer un fichier, on utilise la méthode close()
text.close()


text = open("Étape 3/text.txt", "rt")
ligne1 = text.readline()
#Pour lire le contenu d'un fichier ligne par ligne, on utilise la méthode readline()
print("\n Voici le contenu du fichier 'text.txt' ligne 1 :")
print(ligne1)


from scapy.all import *

#afficher la version de Scapy
print(f"{conf.version} est la version de Scapy.")

#afficher l'interface réseau utilisée
print(f"{conf.iface} est l'interface réseau utilisée.")

#afficher le nom de l'interface réseau utilisée
print(f"{conf.iface.name} est le nom de l'interface réseau utilisée.")

#afficher la table de routage
print(f"La table de route de {conf.iface.name} est: \n {conf.route}")

#afficher la passerelle par défaut
print(f"La passerelle par défaut de {conf.iface.name} est: {conf.route.route('0.0.0.0')[2]}")

#créer un paquet IP avec UDP et afficher le résumé et le contenu
packet1 = IP()/UDP()
print(f"Le résumé du paquet est: {packet1.summary()}")

#afficher le contenu du paquet
print(f"Le contenu du paquet est:")
packet1.show()

#définir les adresses IP source et destination
IPs='192.168.1.1'
IPd='192.168.1.254'

paquet2=IP(src=IPs, dst=IPd)/UDP()

#afficher le paquet sans calculer le checksum
print("Le paquet afficher sans le checksum: ")
paquet2.show()
#afficher le paquet en calculant le checksum
print("Le paquet afficher avec le checksum: ")
paquet2.show2()

#Définir les adresses MAC source et destination
MACs='11:22:33:44:55:66'
MACd='00:0A:1F:3B:4E:64'
#définir les adresses IP source et destination
IPs='192.168.1.1'
IPd='www.univ-pau.fr'

#créer un paquet Ethernet avec IP et TCP
frm=Ether(src=MACs, dst=MACd)/IP(src=IPs, dst=IPd)/TCP(flags='SA')/"Je comprends la SAE scapy"

#afficher le paquet sans calculer le checksum
frm.show()
#afficher le paquet en calculant le checksum
frm.show2()

#lire un fichier de capture
trames=rdpcap("Wireshark/Ping_Google.pcapng")
#afficher le contenu du fichier de capture
print("La capture comprend les paquets suivants :\n")
trames.summary()

#créer un dictionnaire avec les noms et les rôles des personnes
RT={'Siami' : 'chef de departement', 'Bascou' :'enseignant', 'Rivenq' :'secretaire' }

#ajouter une nouvelle personne au dictionnaire
RT['Gallon']='enseignant'

#afficher le nom et le rôle de chaque personne
[print(f"Mr {nom} est {RT[nom]} au département R&T de l'IUT de Mont de Marsan")
for nom in RT]

#créer un dictionnaire avec les noms, les rôles et les années de recrutement des personnes
RT={'Siami' : {'fonction' : 'chef de departement', 'année de recutement' :2002, \
'Enseignant en' : 'Electronique, Programmation'},

#definir une nouvelle personne avec ses informations
'Bascou' : {'fonction' : 'DE 1ere annee de BUT', 'année de recutement' : 2000, \
'Enseignant en' : 'Réseaux'}}

#afficher le nom et role de Mr Bascou
print(f'Le nom de la fonction de Mr Bascou est {RT["Bascou"]["fonction"]}')


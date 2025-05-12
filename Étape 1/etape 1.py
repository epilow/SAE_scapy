from scapy.all import *

#afficher la version de Scapy
print(f"{conf.version} est la version de Scapy.")

#afficher l'interface réseau utilisée
print(f"{conf.iface} est l'interface réseau utilisée.")

#afficher le nom de l'interface réseau utilisée
#print(f"{conf.iface.name} est le nom de l'interface réseau utilisée.")

#afficher la table de routage
print(f"La table de route de {conf.iface} est: \n {conf.route}")

#afficher la passerelle par défaut
print(f"La passerelle par défaut de {conf.iface} est: {conf.route.route('0.0.0.0')[2]}")

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

print('La premiere trame est la suivante :')
trames[0]

trames[2][IP]

trames[2][IP].dst

trames[2][Raw].load

trames[2][Raw].load.split(sep=None)

trames[2][Raw].load.split(sep=None)[2]

trames[2][Raw].load.split(sep=None)[2].decode('UTF8')

ping=IP(dst='8.8.8.8')/ICMP()/"On peut ajouter ici des données à émettre avec le ping"
send(ping)

#envoyer un ping avec plusieur arguments
#send(ping, loop=1)

#envoyer un ping avec une boucle infinie
#send(ping, loop=1, inter=1)

trameping=Ether()/IP(dst='10.2.12.4')/ICMP()/"On peut ajouter ici des données à émettre avec le ping"
sendp(trameping, iface="wlp19s0")

ping=IP(dst='10.    2.12.4')/ICMP()/"On peut ajouter ici des données à émettre avec le ping"
sr(ping)

ping=IP(dst='10.2.12.4')/ICMP()/"On peut ajouter ici des données à émettre avec le ping"
ok, nonok = srloop(ping, count=10, inter=1)

ICMP_types = { 0 : 'Echo-Reply', 3 : 'Destination Unreachable', 8 : 'Echo'}
def print_icmp (packet) :
    type = packet[ICMP].type
    ips = packet[IP].src
    ipd = packet[IP].dst
    if ips==iface_ip :
        print(f"Emission d'un paquet ICMP {ICMP_types[type]} vers {ipd}")
    else :
        print(f"Réception d'un paquet ICMP {ICMP_types[type]} en provenance de {ips}")

iface_ip=get_if_addr(conf.iface)
sniff(filter="icmp", prn=print_icmp, store=0, iface='wlp19s0', count=4)

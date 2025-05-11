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


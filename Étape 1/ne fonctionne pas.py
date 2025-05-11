from scapy.all import *

print('La premiere trame est la suivante :')
trames[0]

trames[2][IP]

trames[2][IP].dst

trames[2][Raw].load

trames[2][Raw].load.split(sep=None)

trames[2][Raw].load.split(sep=None)[2]

trames[2][Raw].load.split(sep=None)[2].decode('UTF8')

ping=IP(dst='10.2.12.4')/ICMP()/"On peut ajouter ici des données à émettre avec le ping"
send(ping)

#envoyer un ping avec plusieur arguments
send(ping, loop=1)

#envoyer un ping avec une boucle infinie
send(ping, loop=1, inter=1)

trameping=Ether()/IP(dst='10.2.12.4')/ICMP()/"On peut ajouter ici des données à émettre avec le ping"
sendp(trameping, iface="eno1")

ping=IP(dst='10.2.12.4')/ICMP()/"On peut ajouter ici des données à émettre avec le ping"
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
sniff(filter="icmp", prn=print_icmp, store=0, iface='en0', count=4)
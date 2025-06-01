from scapy.all import rdpcap, TCP, IP, Raw
import re

# Charger la capture réseau
pcap_file = "Wireshark/ftp.pcapng"
packets = rdpcap(pcap_file)

ftp_user = None
ftp_pass = None
ftp_data_ip = None
ftp_data_port = None
ftp_file_data = b""

# Étape 1 : Rechercher USER, PASS et PORT
for pkt in packets:
    if pkt.haslayer(IP) and pkt.haslayer(TCP) and pkt.haslayer(Raw):
        payload = pkt[Raw].load.decode(errors='ignore')

        if payload.startswith("USER"):
            ftp_user = payload.strip()
            print(f"[+] Identifiant : {ftp_user}")

        elif payload.startswith("PASS"):
            ftp_pass = payload.strip()
            print(f"[+] Mot de passe : {ftp_pass}")

        elif payload.startswith("PORT"):
            # Extraire IP et Port depuis la commande PORT
            match = re.search(r'PORT (\d+),(\d+),(\d+),(\d+),(\d+),(\d+)', payload)
            if match:
                ip_parts = match.groups()[0:4]
                p1, p2 = int(match.group(5)), int(match.group(6))
                ftp_data_ip = ".".join(ip_parts)
                ftp_data_port = p1 * 256 + p2
                print(f"[+] Connexion DATA : {ftp_data_ip}:{ftp_data_port}")

# Étape 2 : Rechercher les paquets contenant les données transférées
if ftp_data_ip and ftp_data_port:
    for pkt in packets:
        if pkt.haslayer(IP) and pkt.haslayer(TCP) and pkt.haslayer(Raw):
            ip = pkt[IP]
            tcp = pkt[TCP]

            if (ip.src == ftp_data_ip or ip.dst == ftp_data_ip) and \
               (tcp.sport == ftp_data_port or tcp.dport == ftp_data_port):
                ftp_file_data += pkt[Raw].load

# Résumé
print("\n=== Résumé FTP ===")
print(f"Utilisateur : {ftp_user}")
print(f"Mot de passe : {ftp_pass}")
print(f"Adresse IP pour les données : {ftp_data_ip}")
print(f"Port de données : {ftp_data_port}")

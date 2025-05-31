from scapy.all import rdpcap, TCP, IP, Raw

# Charger la capture
packets = rdpcap("etape_4/telnet-total.pcapng")

# Récupérer les paquets Telnet contenant des données
telnet_packets = [
    pkt for pkt in packets
    if pkt.haslayer(IP) and pkt.haslayer(TCP) and
    (pkt[TCP].sport == 23 or pkt[TCP].dport == 23) and pkt.haslayer(Raw)
]

# Reconstituer le flux de texte
flux = ""
for pkt in telnet_packets:
    try:
        flux += pkt[Raw].load.decode(errors="ignore")
    except:
        continue

# Rechercher les interactions utilisateur
login = None
password = None

# Recherche basée sur des motifs connus
if "login:" in flux.lower():
    login_section = flux.lower().split("login:")[1]
    login = login_section.strip().split("\n")[0].strip()

if "password:" in flux.lower():
    pwd_section = flux.lower().split("password:")[1]
    password = pwd_section.strip().split("\n")[0].strip()

print("\n=== Identifiants Telnet ===")
print(f"Login : {login}")
print(f"Mot de passe : {password}")

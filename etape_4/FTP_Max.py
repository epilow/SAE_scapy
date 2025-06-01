from scapy.all import *
ftp = rdpcap("Wireshark/ftp.pcapng")

def parse_ftp_from_pcapng(packets):

    for pkt in packets:
        # On filtre les paquets TCP contenant des données FTP
        if pkt.haslayer(TCP) and (pkt[TCP].dport == 21 or pkt[TCP].sport == 21):
            if Raw in pkt:
                try:
                    payload = pkt[Raw].load.decode('utf-8', errors='ignore')

                    # Recherche des commandes FTP
                    if "USER" in payload or "PASS" in payload:
                        
                        if "USER" in payload:
                            user = re.search(r"USER (.+?)\r\n", payload)
                            if user:
                                print(f"Nom d'utilisateur : {user.group(1)}")

                        if "PASS" in payload:
                            passwd = re.search(r"PASS (.+?)\r\n", payload)
                            if passwd:
                                print(f"Mot de passe : {passwd.group(1)}")

                except Exception as e:
                    print("Erreur lors du traitement d’un paquet:", e)

parse_ftp_from_pcapng(ftp)
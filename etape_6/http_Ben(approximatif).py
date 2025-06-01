from scapy.all import rdpcap, TCP, IP, Raw
import base64

# Charger le fichier de capture
packets = rdpcap("Wireshark/www-total.pcapng")

# Fonction d'extraction des identifiants HTTP Basic
def extract_http_credentials(payload):
    if "Authorization: Basic" in payload:
        try:
            for line in payload.split("\r\n"):
                if line.lower().startswith("authorization: basic"):
                    b64_credentials = line.split(" ")[2]
                    decoded = base64.b64decode(b64_credentials).decode()
                    return decoded
        except Exception:
            pass
    return None

# Parcourir les paquets à la recherche de trafic HTTP
for pkt in packets:
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
        try:
            raw_data = pkt[Raw].load.decode(errors="ignore")
            if "Authorization: Basic" in raw_data:
                creds = extract_http_credentials(raw_data)
                if creds:
                    print("[+] Identifiants HTTP détectés !")
                    print(f"    → {creds} (login:motdepasse)")
        except Exception:
            continue

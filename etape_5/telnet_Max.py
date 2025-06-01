from scapy.all import *
telnet = rdpcap("Wireshark/telnet-total.pcapng")

def telnet_pcapng(packets):
    state = "waiting_login_prompt"  # états : waiting_login_prompt, reading_login, waiting_password_prompt, reading_password
    login_buffer = ""
    password_buffer = ""

    for pkt in packets:
        if pkt.haslayer(IP) and pkt.haslayer(TCP) and pkt.haslayer(Raw):
            payload = pkt[Raw].load.decode("utf-8", errors="ignore")
            sport = pkt[TCP].sport
            dport = pkt[TCP].dport

            # serveur -> client : on cherche les prompts "login:" ou "password:"
            if sport == 23:  
                if state == "waiting_login_prompt" and "login:" in payload.lower():
                    print("Tentative de connexion Telnet")
                    state = "reading_login"
                    login_buffer = ""

                elif state == "waiting_password_prompt" and "password:" in payload.lower():
                    state = "reading_password"
                    password_buffer = ""

            # client -> serveur : on récupère le login ou password caractère par caractère
            elif dport == 23:
                if state == "reading_login":
                    for c in payload:
                        if c in "\r\n":
                            print(f"Login : {login_buffer}")
                            state = "waiting_password_prompt"
                            break
                        else:
                            login_buffer += c

                elif state == "reading_password":
                    for c in payload:
                        if c in "\r\n":
                            print(f"Mot de passe : {password_buffer}")
                            state = "done"
                            return
                        else:
                            password_buffer += c

telnet_pcapng(telnet)
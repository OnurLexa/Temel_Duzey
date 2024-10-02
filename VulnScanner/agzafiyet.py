import socket

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # 1 saniye
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target_ip = input("hedef ip: ")
    # tarama portları
    ports_to_scan = [21, 22, 23, 25, 80, 443, 8080] # FTP, SSH, TELNET, SMTP, HTTP, HTTPS, HTTP-ALT
    
    print(f"{target_ip} IP adresine tarama baslatılıyor...")
    open_ports = scan_ports(target_ip, ports_to_scan)

    if open_ports:
        print(f"Acık portlar: {', '.join(map(str, open_ports))}")
    else:
        print("Acık port bulunamadı!")
        

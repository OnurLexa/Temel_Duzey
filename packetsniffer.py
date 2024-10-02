from scapy.all import sniff

# paket işleme fonksiyonu
def packet_callback(packet):
    print(packet.summary())

#sniffer başlat
def start_sniffer():
    print("paket dinleyici baslatılıyor")
    sniff(prn=packet_callback, count=10) # 10 tane dinleyecek istersen değiştir

if __name__ == "__main__":
    start_sniffer()

# sniff = belirtilen sayıda paketi dinler

# packet_callback = gelen her paketi özet olarak yazdırır



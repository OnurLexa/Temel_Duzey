from scapy.all import *

# paket işleme fonksiyonu
def packet_handler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type == 0 and pkt.subtype == 8:
            ssid = pkt[Dot11Elt].info.decode()
            bssid = pkt[Dot11].addr3
            print(f"SSID: {ssid}, BSSID: {bssid}")

# snifferi baslat
def start_wifi_sniffer(interface):
    print("wifi ağları taranıyor...")
    sniff(iface=interface, prn=packet_handler, store=0)

if __name__ == "__main__":
    # kullanıcı arayüzü
    iface = input("wifi arayüzünü girin (örnek: wlan0, wlan1, eth0): ")
    start_wifi_sniffer(iface)

import bluetooth
def cihaz_ara():
    print("cihazlar taranıyor...")
    cihazlar = bluetooth.discover_devices(lookup_names=True)

    if cihazlar:
        print("Bulunan cihazlar:")
        for addr, name in cihazlar:
            print(f"{name} - {addr}")
        else:
            print("cihaz bulunamadı...")

if __name__ == "__main__":
    cihaz_ara()
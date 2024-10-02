from cryptography.fernet import Fernet

# anahtar olustur
def gen_key():
    return Fernet.generate_key()

# sifreleme
def enc_data(key, data):
    f = Fernet(key)
    return f.encrypt(data)

# sifre cözme
def dec_data(key, enc_data):
    f = Fernet(key)
    return f.decrypt(enc_data):

# örnek kullanım
if __name__ = "__main__":
    key = gen_key()
    print(f"anahtar: {key.decode()}")

    # sifrelenecek veri
    data = b"bu veriyi sifrelemek istiyoruz."

    # sifrele
    encrypted = enc_data(key, data)
    print(f"sifrelenmis veri: {encrypted}")

    # sifre cöz
    decrypted = dec_data(key, encrypted)
    print(f"cözülmüs veri: {decrypted.decode()}")

import requests
from colorama import init, Fore, Back, Style
from os import system
import platform
import psutil
import random
import string
import ctypes
import time
import sys
from sites import sites

init(autoreset=True)

def clear():
    
    if name == 'nt':
        _ = system('cls')
        
    else:
        _ = system('clear')

banner1= """
▄▄▄█████▓ ▄▄▄        ▄████      ██████  ███▄    █  ██▓  █████▒ █████▒▓█████  ██▀███  
▓  ██▒ ▓▒▒████▄     ██▒ ▀█▒   ▒██    ▒  ██ ▀█   █ ▓██▒▓██   ▒▓██   ▒ ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██  ▀█▄  ▒██░▄▄▄░   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▒████ ░▒████ ░ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ░██▄▄▄▄██ ░▓█  ██▓     ▒   ██▒▓██▒  ▐▌██▒░██░░▓█▒  ░░▓█▒  ░ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░  ▓█   ▓██▒░▒▓███▀▒   ▒██████▒▒▒██░   ▓██░░██░░▒█░   ░▒█░    ░▒████▒░██▓ ▒██▒
  ▒ ░░    ▒▒   ▓▒█░ ░▒   ▒    ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓   ▒ ░    ▒ ░    ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ▒   ▒▒ ░  ░   ░    ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░ ░      ░       ░ ░  ░  ░▒ ░ ▒░
  ░        ░   ▒   ░ ░   ░    ░  ░  ░     ░   ░ ░  ▒ ░ ░ ░    ░ ░       ░     ░░   ░ 
               ░  ░      ░          ░           ░  ░                    ░  ░   ░     
                                                                                     """

print(Fore.LIGHTGREEN_EX + banner1)
time.sleep(0.5)
system('cls')
welcome = Fore.CYAN + "Welcome to TagSniffer..."
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)
time.sleep(0.5)

kullanici_adi = input(Fore.LIGHTRED_EX + "Kullanıcı Adı Gir: ")

for site in sites:
    try:
        url = f"{site}{kullanici_adi}"
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.LIGHTCYAN_EX + f"Mevcut: {url}")
        else:
            print(Fore.LIGHTRED_EX + f"Mevcut Değil: {url}")
    except requests.exceptions.RequestException:
        print(Fore.YELLOW + f"Tespit edilemedi: {site}")
        
input("devam etmek için enter a bas")
            

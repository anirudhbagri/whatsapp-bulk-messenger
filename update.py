import re

import requests
from requests.exceptions import RequestException


def parse_version(version):
    parts = re.findall(r"\d+", version)
    return tuple(int(part) for part in parts) if parts else (0,)

def check_version(current_version):
    url = "https://raw.githubusercontent.com/yunusemretom/whatsapp-bulk-messenger/primary/version.txt"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except RequestException as exc:
        print(f"Güncelleme kontrolü başarısız: {exc}")
        return False

    remote_version = response.text.strip()
    print(f"Yerel sürüm: {current_version}, Uzak sürüm: {remote_version}")

    if parse_version(remote_version) > parse_version(current_version):
        print("Yeni güncelleme var!")
        with open("version.txt", "w", encoding="utf-8") as f:
            f.write(remote_version)
        return True
    
    else:
        print("Güncel sürüm.")
        return False

def get_local_version(file_path="version.txt"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            version = file.read().strip()
            return version
    except FileNotFoundError:
        print("Yerel sürüm dosyası bulunamadı!")
        return None
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return None

def download_latest():
    download_url = "https://raw.githubusercontent.com/yunusemretom/whatsapp-bulk-messenger/primary/main.py"
    try:
        response = requests.get(download_url, timeout=10)
        response.raise_for_status()
    except RequestException as exc:
        print(f"Güncelleme indirilemedi: {exc}")
        return False

    with open("main.py", "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Yeni sürüm indirildi.")
    return True



if __name__ == "__main__":
       
    print("Güncelleme mevcut, indiriliyor...")
    download_latest()

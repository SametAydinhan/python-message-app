# maksimum 3 dosya eklendiği için readme dosyasını ekleyemedim o yüzden buraya github linki olarak bırakıyorum https://github.com/SametAydinhan/python-message-app

import subprocess
import time

def start_server_and_clients():
    """Sunucuyu ve 3 istemciyi başlatır."""
    try:
        # Sunucuyu başlat
        print("[BAŞLATILIYOR] Sunucu...")
        subprocess.Popen(["python", "server.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

        # Sunucunun tamamen hazır olması için kısa bir bekleme
        time.sleep(2)

        # 3 istemciyi başlat
        for i in range(3):
            print(f"[BAŞLATILIYOR] İstemci {i + 1}...")
            subprocess.Popen(["python", "client.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

        print("[BAŞLATILDI] Sunucu ve istemciler çalışıyor.")
        print("Programı sonlandırmak için ana pencerede CTRL+C yapabilirsiniz.")
    except Exception as e:
        print(f"[HATA] Program başlatılamadı: {e}")

if __name__ == "__main__":
    start_server_and_clients()

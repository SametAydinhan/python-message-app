# İstemci-Sunucu Mesajlaşma Sistemi

Bu proje, 3 istemci ve 1 sunucunun haberleşmesini sağlayan bir istemci-sunucu uygulamasıdır. Proje, iki temel senaryoyu destekler:

1. **Broadcast Mesajlaşma:** Bir istemci tarafından gönderilen mesaj, sunucu aracılığıyla diğer tüm istemcilere iletilir.
2. **Unicast Mesajlaşma:** Bir istemci, belirli bir diğer istemciye özel bir mesaj gönderir.

---

## Proje Geliştiricisi

**Abdülsamet Aydınhan**

---

## Dosya Yapısı

proje/ ├── main.py # Sunucu ve istemcileri otomatik başlatan betik ├── server.py # Sunucu kodu ├── client.py # İstemci kodu └── README.md # Bu dosya

---
## Kullanım Adımları

### Seneryo 1: Broadcast Mesajlaşma

1. İstemci terminalinde 1 seçimini yapın.
2. Göndermek istediğiniz mesajı yazın.
3. Enter tuşuna bastığınızda mesajınız tüm istemcilere iletilecektir.

---
### Seneryo 2: Unicast Mesajlaşma 

1. İstmeci terminalinde 2 seçimini yapın.
2. Hedef istemcinin adını yazın.
3. Göndermek istediğiniz mesajınızı yazın.
4. Mesajınız yanlızca o isme sahip istemciye gönderilecektir.

---

## Programı Sonlandırma

İstemcilerde çıkış yazarak bağlantıyı kapatabilirsiniz

---

## Notlar

- Bu program yalnızca metin tabanlıdır ve komut satırında çalıştırılabilir.
- Unicast mesaj göndermek için doğru istemci adını girdiğinizden emin olun.
- Broadcast mesaj tüm istemcilere gönderilecektir.


---

### **2. Ödevi Senaryoları Çalıştıracak Betik Dosyası**

Bu betik dosyası, senaryoları sırasıyla çalıştırmanızı sağlar.

#### **Senaryoları Başlatıcı Kod (`scenario_runner.py`)**

```python
import os
import time
import subprocess

def run_scenarios():
    """Senaryoları sırasıyla çalıştırır."""
    # 1. Sunucu ve istemcileri başlat
    print("[BAŞLATILIYOR] Sunucu ve istemciler...")
    subprocess.Popen(["python", "server.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    time.sleep(2)  # Sunucu başlatılmasını bekle

    clients = []
    for i in range(3):
        clients.append(subprocess.Popen(["python", "client.py"], creationflags=subprocess.CREATE_NEW_CONSOLE))
    time.sleep(2)

    print("[SENARYO 1] Broadcast mesaj gönderiliyor...")
    print("Bir istemcide aşağıdaki işlemleri yapın:")
    print("1. '1' seçeneğini seçin (Broadcast).")
    print("2. Mesajınızı yazın ve Enter'a basın.")
    time.sleep(10)

    print("[SENARYO 2] Unicast mesaj gönderiliyor...")
    print("Bir istemcide aşağıdaki işlemleri yapın:")
    print("1. '2' seçeneğini seçin (Unicast).")
    print("2. Alıcı istemcinin adını girin.")
    print("3. Mesajınızı yazın ve Enter'a basın.")
    time.sleep(10)

    print("[TAMAMLANDI] Tüm senaryolar çalıştırıldı. Programı elle kapatabilirsiniz.")

if __name__ == "__main__":
    run_scenarios()
```
---

## Nasıl Kullanılır?
1. Seneryo çalıştırma betiğini başlatın python scenario_runner.py
2. Betik sizi yönlendirecektir.
3. Betik çalışmayı tamamladığında tüm seneryolar test edilmiş olacaktır.

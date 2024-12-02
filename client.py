# maksimum 3 dosya eklendiği için readme dosyasını ekleyemedim o yüzden buraya github linki olarak bırakıyorum https://github.com/SametAydinhan/python-message-app

import socket
import threading

# Sunucu bilgileri
HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    """Sunucudan gelen mesajları dinler ve ekranda alt satıra yazdırır."""
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"\n{message.decode()}\n> ", end="")  # Mesajı alt satıra yazdır
        except:
            print("Bağlantı kesildi.")
            break

def main():
    """İstemci ana fonksiyonu."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    client_name = input("Adınızı girin: ")
    client_socket.sendall(client_name.encode())

    # Gelen mesajları dinlemek için bir thread başlat
    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

    print("Mesaj göndermek için aşağıdaki seçeneklerden birini seçin:")
    print("1. Broadcast mesaj gönder (Tüm istemcilere).")
    print("2. Unicast mesaj gönder (Belirli bir alıcıya).")

    try:
        while True:
            print("> ", end="")  # Kullanıcı girişine hazır olduğunu gösterir
            choice = input().strip()  # Kullanıcı seçimini al
            if choice.lower() == "çıkış":
                break

            if choice == "1":
                # Broadcast mesaj
                message = input("Gönderilecek mesajı yazın: ").strip()
                client_socket.sendall(message.encode())
            elif choice == "2":
                # Unicast mesaj
                recipient = input("Hedef alıcının adını girin: ").strip()
                message = input("Gönderilecek mesajı yazın: ").strip()
                unicast_message = f"unicast:{recipient}:{message}"
                client_socket.sendall(unicast_message.encode())
            else:
                print("Geçersiz seçim, lütfen 1 veya 2 seçin.")
    except KeyboardInterrupt:
        print("\nBağlantı sonlandırılıyor...")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()

import socket
import threading

# Sunucu bilgileri
HOST = '127.0.0.1'
PORT = 12345

clients = {}  # {client_name: client_socket}
client_addresses = {}  # {client_socket: client_name}

def broadcast(message, sender_socket=None):
    """Mesajı tüm istemcilere gönder."""
    for client_socket in clients.values():
        if client_socket != sender_socket:
            client_socket.sendall(message)

def unicast(message, recipient_name):
    """Mesajı belirtilen alıcıya gönder."""
    if recipient_name in clients:
        recipient_socket = clients[recipient_name]
        recipient_socket.sendall(message)

def handle_client(client_socket, client_address):
    """İstemci bağlantısını yönet."""
    try:
        # İstemcinin adını al
        client_name = client_socket.recv(1024).decode()
        clients[client_name] = client_socket
        client_addresses[client_socket] = client_name
        print(f"[BAĞLANDI] {client_name} ({client_address})")

        # Mesajları dinle
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode()
            print(f"[MESAJ] {client_name}: {message}")

            if message.startswith("unicast:"):
                _, recipient_name, content = message.split(":", 2)
                unicast(f"[ÖZEL {client_name} -> {recipient_name}]: {content}".encode(), recipient_name)
            else:
                broadcast(f"[{client_name}]: {message}".encode(), sender_socket=client_socket)

    except Exception as e:
        print(f"[HATA] {client_name}: {e}")

    finally:
        # Bağlantıyı temizle
        print(f"[ÇIKIŞ] {client_name} ({client_address})")
        if client_socket in client_addresses:
            del clients[client_addresses[client_socket]]
            del client_addresses[client_socket]
        client_socket.close()

def start_server():
    """Sunucuyu başlat."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[BAŞLADI] Sunucu {HOST}:{PORT} üzerinde çalışıyor.")

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()

if __name__ == "__main__":
    start_server()

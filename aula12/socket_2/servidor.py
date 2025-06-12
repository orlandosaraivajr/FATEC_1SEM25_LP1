import socket
import threading

# Função para lidar com cada cliente
def handle_client(conn, addr):
    print(f"[Conectado] {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            nome = data.decode('utf-8').strip()
            print(f"[{addr}] Nome recebido: {nome}")
        except ConnectionResetError:
            break
    print(f"[Desconectado] {addr}")
    conn.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # localhost
    PORT = 5000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[Servidor iniciado] Escutando em {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

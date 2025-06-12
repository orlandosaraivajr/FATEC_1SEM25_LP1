import socket

HOST = '127.0.0.1'
PORT = 4999

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        try:
            client.connect((HOST, PORT))
            print(f"Conectado ao servidor {HOST}:{PORT}")

            while True:
                nome = input("Digite um nome (ou 'sair' para encerrar): ")
                if nome.lower() == 'sair':
                    break
                client.sendall(nome.encode('utf-8'))

        except ConnectionRefusedError:
            print("Não foi possível conectar ao servidor. Verifique se está em execução.")

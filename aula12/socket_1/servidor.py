import socket

HOST = '127.0.0.1'
PORT = 4999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print(f"Servidor aguardando conexão em {HOST}:{PORT}...")

    conexao, endereco = servidor.accept()
    print(f"Conectado por {endereco}")

    with conexao:
        while True:
            dados = conexao.recv(1024)
            if not dados:
                break
            nome = dados.decode('utf-8').strip()
            if nome.lower() == "sair":
                print("Cliente solicitou encerramento.")
                break
            print(f"Nome recebido: {nome}")

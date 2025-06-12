// cliente_cpp.cpp
#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    const char* SERVER_IP = "127.0.0.1";
    const int SERVER_PORT = 5000;

    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        std::cerr << "Erro ao criar socket.\n";
        return 1;
    }

    sockaddr_in server{};
    server.sin_family = AF_INET;
    server.sin_port = htons(SERVER_PORT);
    inet_pton(AF_INET, SERVER_IP, &server.sin_addr);

    if (connect(sock, (sockaddr*)&server, sizeof(server)) < 0) {
        std::cerr << "Erro ao conectar ao servidor.\n";
        return 1;
    }

    std::string nome;
    std::cout << "Digite um nome para enviar ao servidor: ";
    std::getline(std::cin, nome);

    send(sock, nome.c_str(), nome.length(), 0);
    std::cout << "Nome enviado com sucesso!\n";

    close(sock);
    return 0;
}

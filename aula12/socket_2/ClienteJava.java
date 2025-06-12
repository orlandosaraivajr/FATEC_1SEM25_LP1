// ClienteJava.java
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class ClienteJava {
    public static void main(String[] args) {
        final String HOST = "127.0.0.1";
        final int PORT = 5000;

        try (Socket socket = new Socket(HOST, PORT);
             OutputStream output = socket.getOutputStream();
             PrintWriter writer = new PrintWriter(output, true);
             Scanner scanner = new Scanner(System.in)) {

            System.out.print("Digite um nome para enviar ao servidor: ");
            String nome = scanner.nextLine();
            writer.println(nome);

            System.out.println("Nome enviado com sucesso!");
        } catch (Exception e) {
            System.err.println("Erro: " + e.getMessage());
        }
    }
}

// Servidor.java
import java.net.*;
import java.io.*;

public class Server {

    public static void main(String[] args) {
        ServerSocket server = null;
        Socket connection = null;
        final int port = 5000;

        DataInputStream inp;
        DataOutputStream out;

        try {
            server = new ServerSocket(port);
            System.out.println("Servidor iniciado");

            while (true) {
                connection = server.accept();

                inp = new DataInputStream(connection.getInputStream());
                out = new DataOutputStream(connection.getOutputStream());

                String mesage = inp.readUTF();

                System.out.println(mesage);

                out.writeUTF("Hola mundo desde el servidor!");

                connection.close();
                System.out.println("Cliente desconectado");
            }
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}

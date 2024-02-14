// Cliente.java
import java.net.*;
import java.io.*;

public class Client {
    public static void main(String[] args) {

        final String host = "127.0.0.1";
        final int port = 5000;

        DataInputStream in;
        DataOutputStream out;

        try {
            Socket sc = new Socket(host, port);
            System.out.println("Cliente activo");

            in = new DataInputStream(sc.getInputStream());
            out = new DataOutputStream(sc.getOutputStream());

            out.writeUTF("Hola mundo desde el cliente!");
            String mesage = in.readUTF();
            System.out.println(mesage);
            sc.close();
            
            System.out.println("Cliente desconectado");
            
        } catch (Exception e) {
            System.err.println(e);
        }
    }
}

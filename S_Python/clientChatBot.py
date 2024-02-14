import socket  # Importa el módulo socket para la comunicación de red
import threading  # Importa el módulo threading para manejar múltiples hilos de ejecución

# Define el host y el puerto al que el cliente se conectará
host = '127.0.0.1'  # localhost
port = 5555
# Solicita al usuario que ingrese su nombre de usuario
username = input("Enter your username: ")

# Crea un objeto socket para el cliente usando IPv4 y TCP
# (familia de direcciones, socket orientado a la conexion con comunicación bidireccional) 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establece la conexión del cliente con el servidor en el host y puerto especificados
client.connect((host, port))

# Función para recibir mensajes del servidor
def receive_message():
    while True:
        try:
            # Recibe mensajes del servidor (hasta 1024 bytes) y los decodifica como UTF-8
            message = client.recv(1024).decode('utf-8')
            # Si el mensaje recibido es "@username", envía el nombre de usuario al servidor
            if message == "@username":
                client.send(username.encode('utf-8'))
            # Si no, imprime el mensaje recibido
            else:
                print(message)
        except:
            print("An error occurred....")
            client.close()
            break

# Función para escribir mensajes y enviarlos al servidor
def write_message():
    while True:
        # Solicita al usuario que ingrese un mensaje
        message = f"{username}: {input('')}"
        # Codifica el mensaje como UTF-8 y lo envía al servidor
        client.send(message.encode('utf-8'))

# Crea un hilo para recibir mensajes del servidor
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# Crea un hilo para escribir mensajes y enviarlos al servidor
write_thread = threading.Thread(target=write_message)
write_thread.start()

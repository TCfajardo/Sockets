import socket
import threading

host = '127.0.0.1'  # localhost
port = 5555

# Creación del socket del servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
# Vinculación del socket al host y puerto especificados
server.bind((host, port))

# Habilitación del servidor para escuchar conexiones entrantes
server.listen()
print(f"Server running on {host}:{port}")

clients = []
usernames = []

# Función para enviar un mensaje a todos los clientes, excepto al que lo envió
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

# Función para manejar los mensajes entrantes de un cliente específico
def handle_message(client):
    while True:
        try:
            # Recibe un mensaje del cliente
            message = client.recv(1024)
            broadcast(message, client)
        except:
            # Si hay un error al recibir el mensaje, el cliente se desconecta
            index = clients.index(client)
            username = usernames[index]
            # Mensaje de desconexión del usuario
            message1 = f"ChatBot: {username} disconnected".encode('utf-8')
            # Transmite el mensaje de desconexión a todos los clientes
            broadcast(message1, client)

            # Remueve al cliente y su nombre de usuario de las listas
            clients.remove(client)
            usernames.remove(client)
            client.close()
            break

# Función para aceptar conexiones entrantes de clientes
def receive_connections():
    while True:
        # Acepta una conexión entrante
        # devuelve dos valores: el socket del cliente (client) y la dirección del cliente (address)
        client, address = server.accept()

        client.send("@username".encode('utf-8'))
        # Solicita y recibe el nombre de usuario del cliente
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} is connected with {str(address)}")

        # Mensaje de bienvenida al usuario recién conectado
        message = f"ChatBot: {username} joined the chat!".encode('utf-8')
        broadcast(message, client)

        # Envía un mensaje al cliente indicando que está conectado al servidor
        client.send("Connected to server".encode('utf-8'))

        # Nuevo hilo para manejar los mensajes del cliente
        thread = threading.Thread(target=handle_message, args=(client,))
        thread.start()

# Llamada a la función para aceptar conexiones entrantes
receive_connections()

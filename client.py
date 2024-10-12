import socket

HOST = 'localhost'
PORT = 12345

# Criação do socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client.connect((HOST, PORT))

# Recebe e envia mensagens do servidor
while True:
    data = client.recv(1024).decode()
    print(data)

    if "Sua vez!" in data:
        move = input("Digite sua jogada (linha,coluna): ")
        client.sendall(move.encode())
    elif "Jogo finalizado!" in data:
        break

client.close()

import socket

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5555))  # IP do servidor (localhost para testes locais)

    while True:
        try:
            # Receber mensagem do servidor
            message = client.recv(1024).decode()
            print(message)

            if "Fim do jogo" in message:
                break  # Sair se o jogo terminar

            # Se for a vez do jogador, solicitar as coordenadas
            if "Sua vez" in message:
                r1 = input("Digite a linha inicial: ")
                client.send(r1.encode())
                c1 = input("Digite a coluna inicial: ")
                client.send(c1.encode())
                r2 = input("Digite a linha final: ")
                client.send(r2.encode())
                c2 = input("Digite a coluna final: ")
                client.send(c2.encode())
        except Exception as e:
            print(f"Erro: {e}")
            break

    client.close()

if __name__ == "__main__":
    client_program()

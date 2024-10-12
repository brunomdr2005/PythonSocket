import socket
import threading

# Configuração do servidor
HOST = 'localhost'
PORT = 12345

# Tabuleiro inicial (3x3)
board = [['.' for _ in range(3)] for _ in range(3)]
current_player = 1

# Função para imprimir o tabuleiro
def print_board():
    board_str = ""
    for row in board:
        board_str += " ".join(row) + "\n"
    return board_str

# Função para verificar se a jogada é válida
def is_valid_move(row, col):
    return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '.'

# Função para verificar se o jogo terminou
def is_game_over():
    for row in board:
        if '.' in row:
            return False
    return True

# Função para lidar com as jogadas dos jogadores
def handle_client(conn, player_num, opponent_conn):
    global current_player
    symbol = 'X' if player_num == 1 else 'O'
    
    conn.sendall(f"Bem-vindo, Jogador {player_num} ({symbol})!\n".encode())

    while True:
        # Verifica se o jogo acabou
        if is_game_over():
            conn.sendall("Jogo finalizado!\n".encode())
            opponent_conn.sendall("Jogo finalizado!\n".encode())
            break

        if current_player == player_num:
            conn.sendall(print_board().encode())
            conn.sendall("Sua vez! Escolha linha e coluna (ex: 1,2):\n".encode())
            move = conn.recv(1024).decode().strip()

            try:
                row, col = map(int, move.split(","))
                if is_valid_move(row, col):
                    # Atualiza o tabuleiro
                    board[row][col] = symbol
                    # Alterna o turno
                    current_player = 2 if player_num == 1 else 1
                    conn.sendall("Jogada válida!\n".encode())
                    opponent_conn.sendall("Oponente jogou! Sua vez.\n".encode())
                else:
                    conn.sendall("Movimento inválido. Tente novamente.\n".encode())
            except:
                conn.sendall("Formato inválido. Use: linha,coluna (ex: 1,2)\n".encode())
        else:
            conn.sendall("Aguarde sua vez...\n".encode())

    conn.close()

# Função principal do servidor
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(2)
    print("Servidor iniciado, aguardando conexões...")

    # Aceita dois jogadores
    conn1, addr1 = server.accept()
    print(f"Jogador 1 conectado de {addr1}")
    conn2, addr2 = server.accept()
    print(f"Jogador 2 conectado de {addr2}")

    # Cria uma thread para cada jogador
    threading.Thread(target=handle_client, args=(conn1, 1, conn2)).start()
    threading.Thread(target=handle_client, args=(conn2, 2, conn1)).start()

if __name__ == "__main__":
    start_server()

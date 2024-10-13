import socket
import threading

class DotsAndBoxes:
    def __init__(self, size):
        self.size = size
        self.horizontal_lines = [[False for _ in range(size - 1)] for _ in range(size)]
        self.vertical_lines = [[False for _ in range(size)] for _ in range(size - 1)]
        self.scores = {1: 0, 2: 0}
        self.current_player = 1

    def print_board(self):
        board_str = ""
        for row in range(self.size):
            # Imprimir pontos e linhas horizontais
            for col in range(self.size - 1):
                board_str += "o"
                if self.horizontal_lines[row][col]:
                    board_str += "---"
                else:
                    board_str += "   "
            board_str += "o\n"  # Final da linha de pontos
            
            # Imprimir linhas verticais
            if row < self.size - 1:
                for col in range(self.size):
                    if self.vertical_lines[row][col]:
                        board_str += "|     "
                    else:
                        board_str += "      "
                board_str += "\n"
        
        return board_str

    def check_box_completed(self, row, col):
        # Verifica se uma caixa foi completada
        if self.horizontal_lines[row][col] and self.horizontal_lines[row + 1][col] and \
           self.vertical_lines[row][col] and self.vertical_lines[row][col + 1]:
            return True
        return False

    def make_move(self, r1, c1, r2, c2):
        if r1 == r2 and abs(c1 - c2) == 1:  # Linha horizontal
            row = r1
            col = min(c1, c2)
            if self.horizontal_lines[row][col]:
                return False, "Essa linha já foi marcada!"
            self.horizontal_lines[row][col] = True
        elif c1 == c2 and abs(r1 - r2) == 1:  # Linha vertical
            row = min(r1, r2)
            col = c1
            if self.vertical_lines[row][col]:
                return False, "Essa linha já foi marcada!"
            self.vertical_lines[row][col] = True
        else:
            return False, "Movimento inválido!"

        box_completed = False
        for row in range(self.size - 1):
            for col in range(self.size - 1):
                if self.check_box_completed(row, col):
                    self.scores[self.current_player] += 1
                    box_completed = True

        # Se uma caixa foi completada, o jogador joga novamente
        if not box_completed:
            self.current_player = 2 if self.current_player == 1 else 1  # Troca de jogador

        return True, "Jogada válida."

    def game_over(self):
        return all(all(row) for row in self.horizontal_lines) and all(all(row) for row in self.vertical_lines)

def handle_client(client_socket, player_num, game, lock):
    while not game.game_over():
        try:
            with lock:
                if game.current_player == player_num:
                    client_socket.send(f"\nTabuleiro atual:\n{game.print_board()}".encode())
                    client_socket.send(f"Sua vez, Jogador {player_num}. Digite as coordenadas.\n".encode())
                    
                    client_socket.send("Digite a linha inicial: ".encode())
                    r1 = client_socket.recv(1024).decode()
                    client_socket.send("Digite a coluna inicial: ".encode())
                    c1 = client_socket.recv(1024).decode()
                    client_socket.send("Digite a linha final: ".encode())
                    r2 = client_socket.recv(1024).decode()
                    client_socket.send("Digite a coluna final: ".encode())
                    c2 = client_socket.recv(1024).decode()

                    if r1 and c1 and r2 and c2:
                        try:
                            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
                            valid, message = game.make_move(r1, c1, r2, c2)
                            client_socket.send(f"{message}\n".encode())
                        except ValueError:
                            client_socket.send("Erro: coordenadas inválidas.\n".encode())
                    else:
                        client_socket.send("Erro: coordenadas vazias.\n".encode())
                else:
                    client_socket.send("Aguarde o outro jogador...\n".encode())
        except Exception as e:
            print(f"Erro com o jogador {player_num}: {e}")
            break

    # Mensagem de fim de jogo
    winner = None
    if game.scores[1] > game.scores[2]:
        winner = 1
    elif game.scores[2] > game.scores[1]:
        winner = 2

    if winner:
        client_socket.send(f"Fim do jogo! Jogador {winner} venceu!\n".encode())
    else:
        client_socket.send(f"Fim do jogo! Empate!\n".encode())

    client_socket.send(f"Placar final:\nJogador 1: {game.scores[1]} | Jogador 2: {game.scores[2]}\n".encode())
    client_socket.close()

def server_program():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(2)
    print("Aguardando jogadores...")

    game = DotsAndBoxes(3)
    lock = threading.Lock()

    # Aceitar dois clientes
    client1, addr1 = server.accept()
    print(f"Jogador 1 conectado de {addr1}")
    client1.send("Você é o Jogador 1\n".encode())

    client2, addr2 = server.accept()
    print(f"Jogador 2 conectado de {addr2}")
    client2.send("Você é o Jogador 2\n".encode())

    # Criar threads para ambos os jogadores
    threading.Thread(target=handle_client, args=(client1, 1, game, lock)).start()
    threading.Thread(target=handle_client, args=(client2, 2, game, lock)).start()

if __name__ == "__main__":
    server_program()

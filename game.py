class Game:
    def __init__(self):
        self.matriz = self.criarTabuleiro()
        self.pontosJogador1 = 0  
        self.pontosJogador2 = 0  
        self.jogadorAtual = 1  
        self.quadradosCompletos = [[False, False], [False, False]]  
        self.jogadorPontuou = False  

    def criarTabuleiro(self):
        return [
            [" ", "A", " ", "B", " ", "C"],
            ["0", "O", " ", "O", " ", "O"],
            [" ", " ", " ", " ", " ", " "],
            ["1", "O", " ", "O", " ", "O"],
            [" ", " ", " ", " ", " ", " "],
            ["2", "O", " ", "O", " ", "O"]
        ]

    def verificarPontuacao(self):
        self.jogadorPontuou = False  
        quadrados = [
            (1, 1), (1, 3),  
            (3, 1), (3, 3)   
        ]
        
        for index, (i, j) in enumerate(quadrados):
            linhaQuadrado = index // 2  # Índice da linha do quadrado
            colunaQuadrado = index % 2  # Índice da coluna do quadrado

            
            if not self.quadradosCompletos[linhaQuadrado][colunaQuadrado]:
                if (self.matriz[i][j+1] == "-" and   # borda superior
                    self.matriz[i+1][j] == "|" and   # borda esquerda
                    self.matriz[i+1][j+2] == "|" and # borda direita
                    self.matriz[i+2][j+1] == "-"):   # borda inferior
                    print(f"Quadrado fechado na posição {i}, {j}!")
                    if self.jogadorAtual == 1:
                        self.pontosJogador1 += 1  # Pontua para o Jogador 1
                    else:
                        self.pontosJogador2 += 1  # Pontua para o Jogador 2
                    self.quadradosCompletos[linhaQuadrado][colunaQuadrado] = True  # Marca o quadrado como completado
                    self.jogadorPontuou = True  # O jogador pontuou, portanto, mantém o turno

    def realizarJogada(self):
        ehValido = False
        print(f"Jogador {self.jogadorAtual}'s vez:")
        
        colunaOrigem = input("Digite a coluna de origem: ")
        linhaOrigem = input("Digite a linha de origem: ")
        colunaFinal = input("Digite a coluna de destino: ")
        linhaFinal = input("Digite a linha de destino: ")

       
        if (colunaOrigem.lower() == "a" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "a" and linhaFinal == "1"):
                self.matriz[2][1] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "a" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "a" and linhaFinal == "0"):
                self.matriz[2][1] = "|"
                ehValido = True        

        if (colunaOrigem.lower() == "a" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "a" and linhaFinal == "2"):
                self.matriz[4][1] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "a" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "a" and linhaFinal == "1"):
                self.matriz[4][1] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "a" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "b" and linhaFinal == "0"):
                self.matriz[1][2] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "a" and linhaFinal == "0"):
                self.matriz[1][2] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "c" and linhaFinal == "0"):
                self.matriz[1][4] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "c" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "b" and linhaFinal == "0"):
                self.matriz[1][4] = "-"
                ehValido = True        

        if (colunaOrigem.lower() == "b" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.matriz[2][3] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "0"):
                self.matriz[2][3] = "|"
                ehValido = True        

        if (colunaOrigem.lower() == "c" and linhaOrigem == "0"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.matriz[2][5] = "|"
                ehValido = True 

        if (colunaOrigem.lower() == "c" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "0"):
                self.matriz[2][5] = "|"
                ehValido = True               
        
        if (colunaOrigem.lower() == "a" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.matriz[3][2] = "-"
                ehValido = True
                
        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "a" and linhaFinal == "1"):
                self.matriz[3][2] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.matriz[3][4] = "-"
                ehValido = True

        if (colunaOrigem.lower() == "c" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.matriz[3][4] = "-"
                ehValido = True        

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "b" and linhaFinal == "2"):
                self.matriz[4][3] = "|"
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "b" and linhaFinal == "1"):
                self.matriz[4][3] = "|"
                ehValido = True        

        if (colunaOrigem.lower() == "c" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "2"):
                self.matriz[4][5] = "|"
                ehValido = True 

        if (colunaOrigem.lower() == "c" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.matriz[4][5] = "|"
                ehValido = True         

        if (colunaOrigem.lower() == "b" and linhaOrigem == "1"):
            if (colunaFinal.lower() == "c" and linhaFinal == "2"):
                self.matriz[3][5] = "-" 
                ehValido = True

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "c" and linhaFinal == "1"):
                self.matriz[3][5] = "-" 
                ehValido = True        

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "c" and linhaFinal == "2"):
                self.matriz[5][4] = "-"  
                ehValido = True

        if (colunaOrigem.lower() == "c" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "b" and linhaFinal == "2"):
                self.matriz[5][4] = "-"  
                ehValido = True        

        if (colunaOrigem.lower() == "a" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "b" and linhaFinal == "2"):
                self.matriz[5][2] = "-"  
                ehValido = True  

        if (colunaOrigem.lower() == "b" and linhaOrigem == "2"):
            if (colunaFinal.lower() == "a" and linhaFinal == "2"):
                self.matriz[5][2] = "-"  
                ehValido = True                

        if (ehValido):
            print("Jogada Válida!")
            self.verificarPontuacao()  
            if not self.jogadorPontuou:  
                self.jogadorAtual = 2 if self.jogadorAtual == 1 else 1
        else:
            print("Jogada Inválida")

    def showTabuleiro(self):
        for linha in self.matriz:
            for elemento in linha:
                print(elemento, end=" ")
            print()
        print(f"Pontos do Jogador 1: {self.pontosJogador1} | Pontos do Jogador 2: {self.pontosJogador2}")


game = Game()

while True:
    game.showTabuleiro()
    game.realizarJogada()
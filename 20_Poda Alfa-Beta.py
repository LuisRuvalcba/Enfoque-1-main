import math

# Definimos el tablero del juego del Gato
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()

# Función para verificar si hay un ganador o si el tablero está lleno
def game_over(board):
    # Verifica filas y columnas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-' or board[0][i] == board[1][i] == board[2][i] != '-':
            return True, board[i][0]
    # Verifica diagonales
    if board[0][0] == board[1][1] == board[2][2] != '-' or board[0][2] == board[1][1] == board[2][0] != '-':
        return True, board[1][1]
    # Verifica si el tablero está lleno
    if all(board[i][j] != '-' for i in range(3) for j in range(3)):
        return True, None
    return False, None

# Función para evaluar la utilidad del tablero para el jugador dado
def evaluate(board, player):
    _, winner = game_over(board)
    if winner == player:
        return 1
    elif winner is None:
        return 0
    else:
        return -1

# Función Minimax con poda alfa-beta
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or game_over(board)[0]:
        return evaluate(board, 'O')
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
                    board[i][j] = '-'
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
                    board[i][j] = '-'
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Función para encontrar la mejor jugada utilizando Minimax con poda alfa-beta
def find_best_move_alpha_beta(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'O'
                eval = minimax_alpha_beta(board, 9, alpha, beta, False)
                board[i][j] = '-'
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
                alpha = max(alpha, eval)
    return best_move

# Simulamos el juego del Gato utilizando Minimax con poda alfa-beta
while not game_over(board)[0]:
    print_board(board)
    player_move = input("Ingresa tu movimiento (fila,columna): ")
    row, col = map(int, player_move.split(','))
    board[row][col] = 'X'
    if game_over(board)[0]:
        break
    print("Turno de la IA...")
    ai_move = find_best_move_alpha_beta(board)
    board[ai_move[0]][ai_move[1]] = 'O'

print_board(board)
winner = game_over(board)[1]
if winner:
    print(f"Ganador: {winner}")
else:
    print("Empate")

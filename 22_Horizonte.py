# Función para evaluar la utilidad del tablero para el jugador dado en el juego de Nim
def evaluate_nim(board):
    return sum(board)

# Función Minimax con corte de búsqueda por efecto horizonte para el juego de Nim
def minimax_with_horizon_nim(board, depth, maximizing_player):
    if depth == 0:
        return evaluate_nim(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(len(board)):
            if board[i] > 0:
                for j in range(1, board[i] + 1):
                    new_board = board[:]
                    new_board[i] -= j
                    eval = minimax_with_horizon_nim(new_board, depth - 1, False)
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(len(board)):
            if board[i] > 0:
                for j in range(1, board[i] + 1):
                    new_board = board[:]
                    new_board[i] -= j
                    eval = minimax_with_horizon_nim(new_board, depth - 1, True)
                    min_eval = min(min_eval, eval)
        return min_eval

# Simulamos el juego de Nim utilizando Minimax con corte de búsqueda por efecto horizonte
board = [3, 4, 5]
best_move = None
best_score = float('-inf')
for i in range(len(board)):
    if board[i] > 0:
        for j in range(1, board[i] + 1):
            new_board = board[:]
            new_board[i] -= j
            score = minimax_with_horizon_nim(new_board, depth=2, maximizing_player=False)
            if score > best_score:
                best_score = score
                best_move = (i, j)

print("Mejor movimiento:", best_move)

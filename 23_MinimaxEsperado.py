# Función Minimax con posibilidad Minimax Esperado para el juego de Nim
def expected_minimax_nim(board, depth, maximizing_player):
    if depth == 0:
        return sum(board)
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(len(board)):
            if board[i] > 0:
                for j in range(1, board[i] + 1):
                    new_board = board[:]
                    new_board[i] -= j
                    eval = expected_minimax_nim(new_board, depth - 1, False)
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(len(board)):
            if board[i] > 0:
                for j in range(1, board[i] + 1):
                    new_board = board[:]
                    new_board[i] -= j
                    eval = expected_minimax_nim(new_board, depth - 1, True)
                    min_eval = min(min_eval, eval)
        return min_eval

# Simulamos el juego de Nim utilizando Minimax con posibilidad Minimax Esperado
board = [3, 4, 5]
best_score = float('-inf')
best_move = None
for i in range(len(board)):
    if board[i] > 0:
        for j in range(1, board[i] + 1):
            new_board = board[:]
            new_board[i] -= j
            score = expected_minimax_nim(new_board, depth=2, maximizing_player=False)
            if score > best_score:
                best_score = score
                best_move = (i, j)

print("Mejor movimiento:", best_move)

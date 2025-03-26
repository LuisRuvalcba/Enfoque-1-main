# Función Minimax para el juego de Nim
def nim(board):
    if sum(board) == 0:
        return -1
    if max(board) == 0:
        return 1
    for i in range(len(board)):
        if board[i] > 0:
            for j in range(1, board[i] + 1):
                new_board = board[:]
                new_board[i] -= j
                if nim(new_board) == -1:
                    return 1
    return -1

# Simulamos el juego de Nim
board = [3, 4, 5]
winner = nim(board)
if winner == 1:
    print("Ganador: Jugador 1")
else:
    print("Ganador: Jugador 2")

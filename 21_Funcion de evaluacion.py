# Función de evaluación para el juego de Nim
def evaluate_nim(board):
    return sum(board)

# Ejemplo de uso de la función de evaluación para el juego de Nim
board = [3, 4, 5]
print("Puntuacion de la posición del tablero:", evaluate_nim(board))

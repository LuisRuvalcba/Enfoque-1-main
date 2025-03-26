#Sudoku
def is_valid(board, row, col, num):
    # Verifica si es seguro colocar un número en la posición (row, col)
    # Comprueba si el número ya está en la misma fila o columna
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    # Comprueba si el número ya está en el mismo cuadro 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def backtracking_sudoku(board):
    # Encuentra una celda vacía
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # Intenta colocar un número en la celda vacía
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        # Si es seguro colocar el número, lo colocamos y continuamos con la siguiente celda
                        board[i][j] = num
                        if backtracking_sudoku(board):
                            return True
                        # Si no es posible colocar un número en la siguiente celda con esta configuración, retrocedemos
                        board[i][j] = 0
                # Si no se puede colocar ningún número en esta celda, retornamos falso
                return False
    # Si no hay más celdas vacías, retornamos verdadero (se encontró una solución)
    return True

def solve_sudoku(board):
    if backtracking_sudoku(board):
        # Si se encontró una solución, imprimimos el tablero
        for row in board:
            print(row)
    else:
        print("No hay solucion para el Sudoku.")

# Ejemplo de uso
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
solve_sudoku(sudoku_board)

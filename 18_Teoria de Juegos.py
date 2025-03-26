import random

# Definimos las acciones del juego
actions = ['piedra', 'papel', 'tijera']

# Función para simular una partida
def play_round(player1_action, player2_action):
    if player1_action == player2_action:
        return "Empate"
    elif (player1_action == 'piedra' and player2_action == 'tijera') or \
         (player1_action == 'papel' and player2_action == 'piedra') or \
         (player1_action == 'tijera' and player2_action == 'papel'):
        return "Jugador 1 gana"
    else:
        return "Jugador 2 gana"

# Simulamos una partida aleatoria
player1_action = random.choice(actions)
player2_action = random.choice(actions)
result = play_round(player1_action, player2_action)
print(f"Jugador 1 elige: {player1_action}")
print(f"Jugador 2 elige: {player2_action}")
print(f"Resultado: {result}")

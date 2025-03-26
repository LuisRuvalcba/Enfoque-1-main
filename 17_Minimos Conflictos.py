import random

def initial_state(graph, colors):
    """Genera un estado inicial aleatorio para el problema de asignación de colores."""
    state = {}
    for node in graph:
        state[node] = random.choice(colors)
    return state

def conflicts(graph, state):
    """Calcula el numero de conflictos en el estado actual."""
    conflicts = 0
    for node in graph:
        for neighbor in graph[node]:
            if state[node] == state[neighbor]:
                conflicts += 1
    return conflicts // 2  # Cada conflicto se cuenta dos veces

def min_conflicts(graph, colors, max_steps=1000):
    """Resuelve el problema de asignacion de colores utilizando el algoritmo Min-Conflict."""
    state = initial_state(graph, colors)
    for _ in range(max_steps):
        if conflicts(graph, state) == 0:
            return state  # El estado actual es una solución
        # Selecciona un nodo en conflicto y cambia su color al color con el mínimo conflicto
        node = random.choice(list(graph.keys()))
        min_conflict_value = float('inf')
        min_conflict_color = state[node]
        for color in colors:
            if color != state[node]:
                state[node] = color
                conflict_value = conflicts(graph, state)
                if conflict_value < min_conflict_value:
                    min_conflict_value = conflict_value
                    min_conflict_color = color
        state[node] = min_conflict_color
    return None  # No se encontró una solución en el número máximo de pasos

# Definimos el grafo y los colores disponibles
graph = {'A': ['B', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['B', 'C']}
colors = ['rojo', 'verde', 'azul']

# Resolvemos el problema de asignación de colores utilizando Min-Conflict
solution = min_conflicts(graph, colors)
if solution:
    print("Solucion encontrada:", solution)
else:
    print("No se encontro una solucion.")

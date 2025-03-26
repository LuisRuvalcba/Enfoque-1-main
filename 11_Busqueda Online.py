def heuristic(node, goal):
    # Función heurística, en este caso, la distancia heurística estimada desde el nodo hasta el objetivo
    return 0  # En este ejemplo, no utilizaremos una heurística, por lo que devolvemos cero

def greedy_best_first_search_online(graph, start, goal):
    # Inicializamos la lista de nodos por explorar con el nodo inicial
    frontier = [(heuristic(start, goal), start)]  # Lista de tuplas (heurística, nodo)
    explored = set()  # Conjunto de nodos explorados
    
    # Mientras haya nodos por explorar
    while frontier:
        # Extraemos el nodo de la frontera con la menor heurística
        _, current_node = frontier.pop(0)
        
        # Si encontramos el objetivo, retornamos True
        if current_node == goal:
            return True  # En una búsqueda online, podemos devolver True cuando encontramos el objetivo
        
        # Exploramos los vecinos del nodo actual
        for neighbor in graph[current_node]:
            if neighbor not in explored:
                # Agregamos el vecino a la frontera con su valor de heurística
                frontier.append((heuristic(neighbor, goal), neighbor))
                # Marcamos el vecino como explorado
                explored.add(neighbor)
    
    # Si no encontramos el objetivo, retornamos False
    return False

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
start_node = 'A'
goal_node = 'F'

if greedy_best_first_search_online(graph, start_node, goal_node):
    print("Se encontro el objetivo.")
else:
    print("No se encontro el objetivo.")

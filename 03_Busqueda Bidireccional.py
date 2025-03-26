def bidirectional_bfs(graph, start, goal):
    # Creamos una cola para la búsqueda desde el nodo inicial
    queue_start = deque([start])
    # Creamos un conjunto para mantener un registro de los nodos visitados desde el nodo inicial
    visited_start = set()
    visited_start.add(start)
    
    # Creamos una cola para la búsqueda desde el nodo objetivo
    queue_goal = deque([goal])
    # Creamos un conjunto para mantener un registro de los nodos visitados desde el nodo objetivo
    visited_goal = set()
    visited_goal.add(goal)
    
    # Mientras haya nodos en ambas colas
    while queue_start and queue_goal:
        # Realizamos una iteración desde el nodo inicial
        current_start = queue_start.popleft()
        # Para cada vecino del nodo actual en el grafo desde el nodo inicial
        for neighbor in graph[current_start]:
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                queue_start.append(neighbor)
        
        # Realizamos una iteración desde el nodo objetivo
        current_goal = queue_goal.popleft()
        # Para cada vecino del nodo actual en el grafo desde el nodo objetivo
        for neighbor in graph[current_goal]:
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                queue_goal.append(neighbor)
    
    # Retornamos los nodos visitados desde el nodo inicial y desde el nodo objetivo
    return visited_start, visited_goal

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
visited_start, visited_goal = bidirectional_bfs(graph, start_node, goal_node

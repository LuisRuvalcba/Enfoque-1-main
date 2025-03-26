def dfs(graph, start, visited=None):
    # Si es la primera llamada a la función, inicializamos el conjunto de nodos visitados
    if visited is None:
        visited = set()
    # Añadimos el nodo actual al conjunto de nodos visitados
    visited.add(start)
    print("Nodo visitado:", start)
    # Para cada vecino del nodo actual
    for neighbor in graph[start]:
        # Si el vecino no ha sido visitado
        if neighbor not in visited:
            # Realizamos una búsqueda en profundidad desde el vecino
            dfs(graph, neighbor, visited)

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
print("Nodos alcanzables desde 'A':")
dfs(graph, start_node)

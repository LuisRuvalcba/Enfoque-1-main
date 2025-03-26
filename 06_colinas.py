def hill_climbing(graph, start, eval_func):
    # Empezamos en el nodo inicial
    current_node = start
    # Iteramos hasta que no podamos mejorar más
    while True:
        # Obtenemos los vecinos del nodo actual
        neighbors = graph[current_node]
        # Evaluamos los vecinos usando la función de evaluación
        neighbor_values = [(neighbor, eval_func(neighbor)) for neighbor in neighbors]
        # Encontramos el vecino con el valor mínimo
        best_neighbor, best_value = min(neighbor_values, key=lambda x: x[1])
        # Si el valor del mejor vecino es menor que el valor del nodo actual, movemos allí
        if best_value < eval_func(current_node):
            current_node = best_neighbor
        else:
            # Si no podemos mejorar más, retornamos el nodo actual
            return current_node

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Definimos una función de evaluación simple basada en la cantidad de conexiones del nodo
def eval_func(node):
    return len(graph[node])

# Empezamos la búsqueda desde el nodo 'A'
start_node = 'A'
local_min = hill_climbing(graph, start_node, eval_func)
print("Minimo local encontrado:", local_min)

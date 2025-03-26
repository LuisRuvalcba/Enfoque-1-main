import random

def tabu_search(graph, start, tabu_size=5, max_iterations=100):
    # Inicializamos la lista tabú vacía
    tabu_list = []
    # Inicializamos el nodo actual como el nodo inicial
    current_node = start
    # Inicializamos el conjunto de nodos alcanzables como el conjunto que contiene el nodo inicial
    reachable_nodes = set([start])
    
    # Iteramos hasta alcanzar el número máximo de iteraciones
    for _ in range(max_iterations):
        # Generamos una lista de vecinos del nodo actual
        neighbors = graph[current_node]
        # Seleccionamos aleatoriamente un vecino que no esté en la lista tabú
        non_tabu_neighbors = [neighbor for neighbor in neighbors if neighbor not in tabu_list]
        if not non_tabu_neighbors:
            # Si no hay vecinos no tabú, salimos del bucle
            break
        next_node = random.choice(non_tabu_neighbors)
        
        # Actualizamos la lista tabú y el nodo actual
        tabu_list.append(next_node)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        current_node = next_node
        
        # Agregamos el nodo actual al conjunto de nodos alcanzables
        reachable_nodes.add(current_node)
    
    return reachable_nodes

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
tabu_size = 3
max_iterations = 100

reachable_nodes = tabu_search(graph, start_node, tabu_size, max_iterations)
print("Nodos alcanzables desde el nodo inicial:", reachable_nodes)

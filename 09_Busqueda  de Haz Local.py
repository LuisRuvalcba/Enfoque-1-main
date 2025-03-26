import random

def beam_search(graph, start, beam_width=2, max_iterations=100):
    # Inicializamos el haz como una lista que contiene solo el nodo inicial
    beam = [[start]]
    # Inicializamos el conjunto de nodos alcanzables como el conjunto que contiene el nodo inicial
    reachable_nodes = set([start])
    
    # Iteramos hasta alcanzar el número máximo de iteraciones
    for _ in range(max_iterations):
        # Creamos un nuevo haz vacío
        new_beam = []
        # Expandimos cada camino en el haz actual
        for path in beam:
            # Obtenemos el último nodo en el camino
            current_node = path[-1]
            # Expandimos el camino agregando los vecinos del último nodo
            neighbors = graph[current_node]
            for neighbor in neighbors:
                new_path = path + [neighbor]
                new_beam.append(new_path)
                # Agregamos el nodo al conjunto de nodos alcanzables
                reachable_nodes.add(neighbor)
        # Seleccionamos los mejores caminos para formar el nuevo haz
        beam = sorted(new_beam, key=lambda x: len(x))[:beam_width]
    
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
beam_width = 2
max_iterations = 100

reachable_nodes = beam_search(graph, start_node, beam_width, max_iterations)
print("Nodos alcanzables desde el nodo inicial:", reachable_nodes)

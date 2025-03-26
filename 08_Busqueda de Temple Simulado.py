import random
import math

def simulated_annealing(graph, start, initial_temperature=100, cooling_rate=0.95, max_iterations=1000):
    # Inicializamos el nodo actual como el nodo inicial
    current_node = start
    # Inicializamos la temperatura inicial
    temperature = initial_temperature
    # Inicializamos el conjunto de nodos alcanzables como el conjunto que contiene el nodo inicial
    reachable_nodes = set([start])
    
    # Iteramos hasta alcanzar el número máximo de iteraciones o hasta que la temperatura sea muy baja
    for _ in range(max_iterations):
        # Obtenemos los vecinos del nodo actual
        neighbors = graph[current_node]
        # Seleccionamos aleatoriamente un vecino
        next_node = random.choice(neighbors)
        
        # Calculamos la diferencia en el costo entre el vecino y el nodo actual
        delta_cost = 1  # Consideramos que el costo de cualquier movimiento es 1
        
        # Si el movimiento es favorable (menor costo) o es aceptado con una probabilidad dada por la temperatura
        if delta_cost < 0 or random.uniform(0, 1) < math.exp(-delta_cost / temperature):
            current_node = next_node
            # Agregamos el nodo actual al conjunto de nodos alcanzables
            reachable_nodes.add(current_node)
        
        # Disminuimos la temperatura según el enfriamiento exponencial
        temperature *= cooling_rate
    
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
initial_temperature = 100
cooling_rate = 0.95
max_iterations = 1000

reachable_nodes = simulated_annealing(graph, start_node, initial_temperature, cooling_rate, max_iterations)
print("Nodos alcanzables desde el nodo inicial:", reachable_nodes)

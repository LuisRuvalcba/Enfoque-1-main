import random

class AlgoritmoGenetico:
    def __init__(self, poblacion_size, genes):
        self.poblacion_size = poblacion_size  # Tamaño de la población
        self.genes = genes  # Genes posibles
        self.poblacion = []  # Población inicial

    def inicializar_poblacion(self):
        # Crea una población inicial de individuos aleatorios
        for _ in range(self.poblacion_size):
            # Genera un individuo con genes aleatorios
            individuo = ''.join(random.choice(self.genes) for _ in range(len(self.genes)))
            self.poblacion.append(individuo)

    def calcular_fitness(self, objetivo):
        # Calcula el fitness de cada individuo en la población basado en su similitud con el objetivo
        fitness = []
        for individuo in self.poblacion:
            # Calcula la similitud entre el individuo y el objetivo
            similitud = sum(1 for gen1, gen2 in zip(individuo, objetivo) if gen1 == gen2)
            # Agrega el fitness a la lista
            fitness.append(similitud)
        return fitness

    def seleccionar_padres(self, fitness):
        # Selecciona dos padres de la población basados en su fitness
        padres = []
        for _ in range(2):
            # Utiliza la ruleta de selección proporcional para elegir un padre
            padre = random.choices(self.poblacion, weights=fitness, k=1)[0]
            padres.append(padre)
        return padres

    def cruzar(self, padre1, padre2):
        # Cruza los genes de dos padres para crear un nuevo individuo
        punto_cruce = random.randint(0, len(self.genes) - 1)
        hijo = padre1[:punto_cruce] + padre2[punto_cruce:]
        return hijo

    def mutar(self, hijo, tasa_mutacion):
        # Mutación aleatoria en el hijo
        for i in range(len(hijo)):
            if random.random() < tasa_mutacion:
                hijo = hijo[:i] + random.choice(self.genes) + hijo[i+1:]
        return hijo

    def evolucionar(self, objetivo, tasa_mutacion, num_generaciones):
        # Evoluciona la población hasta encontrar el objetivo o alcanzar el número máximo de generaciones
        for generacion in range(num_generaciones):
            fitness = self.calcular_fitness(objetivo)
            mejor_fitness = max(fitness)
            mejor_individuo = self.poblacion[fitness.index(mejor_fitness)]
            print(f"Generacion {generacion + 1}: {mejor_individuo} - Fitness: {mejor_fitness}")

            if mejor_fitness == len(objetivo):
                print("Se encontro el objetivo!")
                break

            nueva_generacion = []

            for _ in range(self.poblacion_size // 2):
                # Selecciona dos padres
                padres = self.seleccionar_padres(fitness)
                # Cruza los padres para crear un nuevo individuo
                hijo = self.cruzar(padres[0], padres[1])
                # Aplica mutación al hijo
                hijo = self.mutar(hijo, tasa_mutacion)
                nueva_generacion.append(hijo)

            # Reemplaza la población anterior con la nueva generación
            self.poblacion = nueva_generacion

# Ejemplo de uso
if __name__ == "__main__":
    objetivo = "HELLO"  # Objetivo a alcanzar
    genes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Genes posibles
    poblacion_size = 100  # Tamaño de la población
    tasa_mutacion = 0.1  # Tasa de mutación
    num_generaciones = 1000  # Número máximo de generaciones

    ag = AlgoritmoGenetico(poblacion_size, genes)
    ag.inicializar_poblacion()
    ag.evolucionar(objetivo, tasa_mutacion, num_generaciones)

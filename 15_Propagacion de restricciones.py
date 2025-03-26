from constraint import Problem, AllDifferentConstraint

# Creamos una instancia del problema de satisfacción de restricciones
problem = Problem()

# Definimos las variables del problema, que son los eventos
events = ['Evento1', 'Evento2', 'Evento3', 'Evento4']

# Añadimos las variables al problema, asignando el dominio de horarios (mañana, tarde, noche)
for event in events:
    problem.addVariable(event, ['mañana', 'tarde', 'noche'])

# Añadimos la restricción de que ningún par de eventos tenga el mismo horario
problem.addConstraint(AllDifferentConstraint(), events)

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solution in solutions:
    print(solution)

from constraint import Problem

# Creamos una instancia del problema de satisfacción de restricciones
problem = Problem()

# Definimos las variables del problema, que son los eventos
events = ['Evento1', 'Evento2', 'Evento3', 'Evento4']

# Añadimos las variables al problema, asignando el dominio de horarios (mañana, tarde, noche)
for event in events:
    problem.addVariable(event, ['mañana', 'tarde', 'noche'])

# Añadimos las restricciones al problema, que garantizan que no haya conflictos de horarios entre eventos
problem.addConstraint(lambda x, y: x != y, ('Evento1', 'Evento2'))
problem.addConstraint(lambda x, y: x != y, ('Evento1', 'Evento3'))
problem.addConstraint(lambda x, y: x != y, ('Evento1', 'Evento4'))
problem.addConstraint(lambda x, y: x != y, ('Evento2', 'Evento3'))
problem.addConstraint(lambda x, y: x != y, ('Evento2', 'Evento4'))
problem.addConstraint(lambda x, y: x != y, ('Evento3', 'Evento4'))

# Resolvemos el problema
solutions = problem.getSolutions()

# Imprimimos las soluciones encontradas
for solution in solutions:
    print(solution)

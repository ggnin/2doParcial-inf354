import random
import math

# Definición de las tareas y sus duraciones
tasks = {
    'A': {'duration': 3, 'precedence': []},
    'B': {'duration': 2, 'precedence': ['A']},
    'C': {'duration': 4, 'precedence': ['A']},
    'D': {'duration': 5, 'precedence': ['B', 'C']}
}

# Función para calcular la duración total de un plan dado
def calculate_total_duration(plan):
    total_duration = 0
    for task in plan:
        total_duration += tasks[task]['duration']
    return total_duration

# Función para verificar si un plan cumple con todas las restricciones de precedencia
def satisfies_constraints(plan):
    for task in plan:
        for prec_task in tasks[task]['precedence']:
            if prec_task not in plan[:plan.index(task)]:
                return False
    return True

# Algoritmo de recocido simulado
def simulated_annealing(initial_plan, objective_function, initial_temperature=1000, cooling_rate=0.95, num_iterations=1000):
    current_plan = initial_plan
    best_plan = current_plan
    temperature = initial_temperature
    
    for i in range(num_iterations):
        # Generar un nuevo estado vecino
        new_plan = current_plan[:]
        # Aquí se puede implementar una perturbación como intercambiar dos tareas adyacentes
        idx1 = random.randint(0, len(new_plan)-2)
        idx2 = idx1 + 1
        new_plan[idx1], new_plan[idx2] = new_plan[idx2], new_plan[idx1]
        
        # Calcular el costo (duración total) y verificar las restricciones
        current_cost = objective_function(current_plan)
        new_cost = objective_function(new_plan)
        
        if new_cost < current_cost or random.random() < math.exp((current_cost - new_cost) / temperature):
            current_plan = new_plan
        
        # Actualizar la mejor solución encontrada
        if objective_function(current_plan) < objective_function(best_plan) and satisfies_constraints(current_plan):
            best_plan = current_plan
        
        # Reducir la temperatura
        temperature *= cooling_rate
    
    return best_plan

# Función objetivo (costo) - En este caso, la duración total del proyecto
def objective_function(plan):
    return calculate_total_duration(plan)

# Generar un plan inicial aleatorio
initial_plan = list(tasks.keys())
random.shuffle(initial_plan)

# Ejecutar el recocido simulado
best_plan = simulated_annealing(initial_plan, objective_function)

# Mostrar resultado
print("Mejor plan encontrado:")
print(best_plan)
print("Duración total del proyecto:", objective_function(best_plan))

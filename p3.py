import random

def objective_function(permutation):
    """ Función objetivo: Suma de los elementos de la permutación """
    return sum(permutation)

def generate_initial_solution(n):
    """ Genera una permutación inicial aleatoria de números del 1 al n """
    return random.sample(range(1, n+1), n)

def generate_neighbors(permutation):
    """ Genera todos los vecinos de la permutación intercambiando dos elementos """
    neighbors = []
    length = len(permutation)
    for i in range(length):
        for j in range(i+1, length):
            neighbor = permutation[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def local_search(max_iterations, n):
    """ Búsqueda local para maximizar la función objetivo """
    current_solution = generate_initial_solution(n)
    current_value = objective_function(current_solution)
    best_solution = current_solution[:]
    best_value = current_value
    
    iterations_without_improvement = 0
    while iterations_without_improvement < max_iterations:
        neighbors = generate_neighbors(current_solution)
        found_better = False
        for neighbor in neighbors:
            neighbor_value = objective_function(neighbor)
            if neighbor_value > best_value:
                best_solution = neighbor[:]
                best_value = neighbor_value
                found_better = True
                break
        
        if found_better:
            current_solution = best_solution[:]
            current_value = best_value
            iterations_without_improvement = 0
        else:
            iterations_without_improvement += 1
    
    return best_solution, best_value

# Parámetros
n = 5  # Número de elementos en la permutación (por ejemplo)
max_iterations = 1000  # Máximo número de iteraciones sin mejora

# Ejecución de la búsqueda local
best_solution, best_value = local_search(max_iterations, n)

# Resultados
print("Mejor solucion:", best_solution)
print("Valor óptimo :", best_value)

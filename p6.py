import numpy as np
import random
from itertools import permutations

# Definición del grafo
grafo = {
    'A': {'C': 9, 'B': 7, 'E': 20, 'D': 8},
    'B': {'A': 7, 'C': 10, 'E': 11, 'D': 4},
    'C': {'A': 9, 'B': 10, 'D': 15, 'E': 5},
    'D': {'A': 8, 'B': 4, 'C': 15, 'E': 17},
    'E': {'A': 20, 'B': 11, 'C': 5, 'D': 17}
}

# Lista de nodos (ciudades)
nodos = list(grafo.keys())

# Función para calcular la distancia total de una ruta (permutación)
def calcular_distancia_total(ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        ciudad_actual = ruta[i]
        siguiente_ciudad = ruta[i + 1]
        distancia_total += grafo[ciudad_actual][siguiente_ciudad]
    # Sumar la distancia de regreso a la ciudad inicial
    distancia_total += grafo[ruta[-1]][ruta[0]]
    return distancia_total

# Función para generar una población inicial de rutas
def generar_poblacion_inicial(tamano_poblacion):
    poblacion = []
    for _ in range(tamano_poblacion):
        ruta_aleatoria = random.sample(nodos, len(nodos))
        poblacion.append(ruta_aleatoria)
    return poblacion

# Función de selección de padres basada en el torneo
def seleccion_padres(poblacion, num_padres):
    padres = []
    for _ in range(num_padres):
        muestra_torneo = random.sample(poblacion, 3)
        ganador_torneo = min(muestra_torneo, key=lambda ruta: calcular_distancia_total(ruta))
        padres.append(ganador_torneo)
    return padres

# Función de cruce (crossover) utilizando orden de cruce (OX)
def cruzar_padres(padre1, padre2):
    punto_corte1 = random.randint(0, len(padre1) - 1)
    punto_corte2 = random.randint(punto_corte1 + 1, len(padre1))
    
    hijo = [-1] * len(padre1)
    segmento_padre1 = padre1[punto_corte1:punto_corte2]
    hijo[punto_corte1:punto_corte2] = segmento_padre1
    
    idx_padre2 = 0
    for i in range(len(padre1)):
        if hijo[i] == -1:
            while padre2[idx_padre2] in segmento_padre1:
                idx_padre2 += 1
            hijo[i] = padre2[idx_padre2]
            idx_padre2 += 1
    
    return hijo

# Función de mutación que intercambia dos posiciones en la ruta
def mutar(ruta):
    idx1, idx2 = random.sample(range(len(ruta)), 2)
    ruta[idx1], ruta[idx2] = ruta[idx2], ruta[idx1]

# Algoritmo genético para resolver el TSP
def algoritmo_genetico(grafo, tamano_poblacion, num_generaciones):
    poblacion = generar_poblacion_inicial(tamano_poblacion)
    
    for generacion in range(num_generaciones):
        padres = seleccion_padres(poblacion, num_padres=2)
        descendientes = []
        
        for i in range(0, tamano_poblacion, 2):
            hijo1 = cruzar_padres(padres[0], padres[1])
            hijo2 = cruzar_padres(padres[1], padres[0])
            
            if random.random() < 0.2:
                mutar(hijo1)
            if random.random() < 0.2:
                mutar(hijo2)
            
            descendientes.append(hijo1)
            descendientes.append(hijo2)
        
        poblacion = descendientes
    
    mejor_ruta = min(poblacion, key=lambda ruta: calcular_distancia_total(ruta))
    mejor_distancia = calcular_distancia_total(mejor_ruta)
    
    return mejor_ruta, mejor_distancia

# Ejecutar el algoritmo genético para resolver el TSP
mejor_ruta, mejor_distancia = algoritmo_genetico(grafo, tamano_poblacion=50, num_generaciones=1000)

# Mostrar resultados
print("Mejor ruta encontrada:", mejor_ruta)
print("Distancia de la mejor ruta encontrada:", mejor_distancia)

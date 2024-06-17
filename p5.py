# Definición del grafo
grafo = {
    'A': {'C': 9, 'B': 7, 'E': 20, 'D': 8},
    'B': {'A': 7, 'C': 10, 'E': 11, 'D': 4},
    'C': {'A': 9, 'B': 10, 'D': 15, 'E': 5},  
    'D': {'A': 8, 'B': 4, 'C': 15, 'E': 17},
    'E': {'A': 20, 'B': 11, 'C': 5, 'D': 17}
}

import heapq

def dijkstra(grafo, nodo_origen):
    """
    Implementación del algoritmo de Dijkstra para encontrar el camino más corto desde un nodo origen a todos los demás nodos.
    """
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[nodo_origen] = 0
    cola_prioridad = [(0, nodo_origen)]  # (distancia, nodo)
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return distancias

def comparar_pesos_aristas(grafo, nodo1, nodo2):
    """
    Función para comparar los pesos de las aristas entre dos nodos específicos en el grafo.
    """
    if nodo1 not in grafo or nodo2 not in grafo:
        raise ValueError("Los nodos deben estar presentes en el grafo.")
    
    peso_arista_nodo1_nodo2 = grafo[nodo1].get(nodo2, float('inf'))
    peso_arista_nodo2_nodo1 = grafo[nodo2].get(nodo1, float('inf'))
    
    return {
        f"Peso de arista {nodo1}-{nodo2}": peso_arista_nodo1_nodo2,
        f"Peso de arista {nodo2}-{nodo1}": peso_arista_nodo2_nodo1
    }

# Ejemplo de uso de Dijkstra para encontrar el camino más corto desde 'A'
ruta_corta_desde_A = dijkstra(grafo, 'A')
print("Ruta más corta desde A:", ruta_corta_desde_A)

# Ejemplo de comparación de pesos de aristas entre 'A' y 'B'
pesos_aristas_A_B = comparar_pesos_aristas(grafo, 'A', 'B')
print("Comparación de pesos de aristas entre A y B:")
print(pesos_aristas_A_B)

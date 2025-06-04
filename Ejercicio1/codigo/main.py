import random
import time
import copy

# Importar todas las funciones de ordenamiento
from metodos_ordenamiento.shell import shell_sort
from metodos_ordenamiento.selección import selection_sort
from metodos_ordenamiento.rapido import quick_sort
from metodos_ordenamiento.mergeo import merge_sort
from metodos_ordenamiento.inserción import insertion_sort
from metodos_ordenamiento.burbujeo import bubble_sort
from metodos_ordenamiento.bubujeo_optimizado import bubble_sort_opt

def generar_array(tamaño):
    """Crea un array aleatorio"""
    return [random.randint(1, tamaño) for _ in range(tamaño)]

def probar_ordenamiento(funcion, nombre, array):
    """Prueba un método de ordenamiento y mide el tiempo"""
    print(f"\n--- Probando {nombre} ---")
    array_copia = copy.deepcopy(array)
    
    inicio = time.perf_counter()
    funcion(array_copia)
    fin = time.perf_counter()
    
    tiempo = fin - inicio
    print(f"Tiempo: {tiempo:.8f} segundos")

def main():
    print("Comparando métodos de ordenamiento")
    print("=" * 50)
    
    # Los métodos que vamos a probar
    metodos = [
        (shell_sort, "Shell"),
        (quick_sort, "Rápido"),
        (merge_sort, "Mergeo"),
        (insertion_sort, "Inserción"),
        (selection_sort, "Selección"), 
        (bubble_sort, "Burbujeo"),
        (bubble_sort_opt, "Burbujeo Optimizado")
    ]
    
    # Tamaños de arrays para probar
    tamaños = [10, 100, 1000, 10000, 100000, 1000000]
    
    for tamaño in tamaños:
        print(f"\nArrays de {tamaño:,} elementos")
        print("-" * 40)
        
        # Generar un array aleatorio
        array = generar_array(tamaño)
        
        # Probar cada método
        for funcion, nombre in metodos:
            try:
                probar_ordenamiento(funcion, nombre, array)
            except Exception as e:
                print(f"\n--- {nombre} ---")
                print(f"Error: {e}")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    print("Inicio")
    main()
    print("\nCompletado") 
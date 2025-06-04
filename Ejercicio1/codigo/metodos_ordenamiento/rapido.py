# Variable global para contar intercambios
intercambios_quick = 0

def quick_sort(arr):
    global intercambios_quick
    intercambios_quick = 0  # reiniciar contador
    quick_sort_helper(arr, 0, len(arr) - 1)
    print(f"Quick Sort completado. Intercambios realizados: {intercambios_quick}")
    return intercambios_quick
                    
def quick_sort_helper(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort_helper(arr, low, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, high)

def partition(arr, low, high):
    global intercambios_quick
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            intercambios_quick += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    intercambios_quick += 1
    return i + 1
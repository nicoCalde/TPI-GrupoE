# Variable global para contar intercambios
intercambios_merge = 0

def merge_sort(arr):
    global intercambios_merge
    intercambios_merge = 0  # reiniciar contador
    merge_sort_helper(arr)
    print(f"Merge Sort completado. Movimientos realizados: {intercambios_merge}")
    return intercambios_merge

def merge_sort_helper(arr):
    global intercambios_merge
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_helper(left_half)
        merge_sort_helper(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            intercambios_merge += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            intercambios_merge += 1
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            intercambios_merge += 1
            j += 1
            k += 1
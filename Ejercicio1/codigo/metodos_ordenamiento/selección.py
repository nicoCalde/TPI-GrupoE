def selection_sort(arr):
    intercambios = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        intercambios += 1

    print(f"Ordenamiento por selección completado. Total de intercambios: {intercambios}")
    return intercambios
def insertion_sort(arr):
    intercambios = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            intercambios += 1
            j -= 1
        arr[j + 1] = key

    print(f"Insertion Sort completado. Movimientos realizados: {intercambios}")
    return intercambios
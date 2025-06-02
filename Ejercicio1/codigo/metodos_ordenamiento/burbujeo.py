def bubble_sort(arr):
    intercambios = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                intercambios += 1

    print(f"Bubble Sort completado. Intercambios realizados: {intercambios}")
    return intercambios
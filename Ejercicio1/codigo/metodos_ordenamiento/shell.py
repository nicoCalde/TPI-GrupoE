def shell_sort(arr):
    intercambios = 0
    n = len(arr)
    gap = n // 2  

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i

            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                intercambios += 1
                j -= gap
            arr[j] = key
        gap //= 2  

    print(f"Shell Sort completado. Intercambios realizados: {intercambios}")
    return intercambios
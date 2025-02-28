def selection_sort(arr):
    N = len(arr)  # Obtener la longitud del array
    i = 0  # Inicializar índice del bucle exterior

    while i < N - 1:  # Iteramos hasta el penúltimo elemento
        minIndex = i  # Suponemos que el mínimo está en la posición actual
        j = i + 1  # Inicializamos el índice para comparar con el mínimo

        while j < N:  # Bucle para buscar el menor elemento en el resto del array
            if arr[j]["code"] < arr[minIndex]["code"]:  # Comparación basada en el valor de "code"
                minIndex = j  # Actualizamos la posición del mínimo encontrado
            j = j + 1  # Incrementamos j para seguir buscando

        if minIndex != i:  # Si encontramos un mínimo diferente al actual
            temp = arr[i]  # Guardamos el valor de arr[i] en una variable temporal
            arr[i] = arr[minIndex]  # Intercambiamos arr[i] con el mínimo encontrado
            arr[minIndex] = temp  # Asignamos el valor original de arr[i] en su nueva posición

        i = i + 1  # Pasamos al siguiente índice

# Datos de entrada
people = [
    {"name": "Camila", "code": 4},
    {"name": "Daniel", "code": 2},
    {"name": "Sofía", "code": 9},
    {"name": "Juan", "code": 1},
    {"name": "Valentina", "code": 6},
    {"name": "Carlos", "code": 3},
    {"name": "Isabella", "code": 8},
    {"name": "Andrés", "code": 7},
    {"name": "Mariana", "code": 10},
    {"name": "Felipe", "code": 5}
]

# Ordenar la lista
selection_sort(people)

# Mostrar resultado
print(people)

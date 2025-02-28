def insertion_sort(array):
    
    N = len(array)  # n va ser igual a la longitud del array(10)
    i = 1  # se empieza con i desde el segundo  elemento 

    while i < N: # el segundo elemento tiene que ser menor que la longitud del array 
        current = array[i]  # Guardamos el elemento actual
        j = i - 1  # j va ser igual al elmento anteriro

        # mientras j sea mayor/igual a 0 y j sea mayor se sigue moviendo 
        while j >= 0 and array[j]["code"] > current["code"]:
            array[j + 1] = array[j]  # Desplazamos el array (j) hacia la derecha
            j -= 1  # Movemos j  una posicion hacia atrás
        
        array[j + 1] = current  # Insertamos el elemento en la posición correcta
        i += 1  # Pasamos al siguiente elemento

    return array  # Retornamos el array ordenado

estudiantes = [
    {"name": "Camila", "code": 5},
    {"name": "Daniel", "code": 2},
    {"name": "Sofía", "code": 9},
    {"name": "Juan", "code": 1},
    {"name": "Valentina", "code": 7},
    {"name": "Carlos", "code": 3},
    {"name": "Isabella", "code": 8},
    {"name": "Andrés", "code": 4},
    {"name": "Mariana", "code": 10},
    {"name": "Felipe", "code": 6},
]

# Aplicamos el algoritmo
arreglo_ordenado= insertion_sort(estudiantes)

for i in arreglo_ordenado:
    print(i)


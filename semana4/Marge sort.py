import heapq
# Lista de empleados
empleados = [
    {"nombre": "Carlos", "edad": 29, "salario": 3000},
    {"nombre": "Ana", "edad": 25, "salario": 3500},
    {"nombre": "Luis", "edad": 32, "salario": 4000},
    {"nombre": "Marta", "edad": 28, "salario": 3200},
    {"nombre": "Pedro", "edad": 35, "salario": 4200},
    {"nombre": "Elena", "edad": 27, "salario": 2800},
    {"nombre": "Sofía", "edad": 30, "salario": 3100},
    {"nombre": "Javier", "edad": 26, "salario": 3300},
]

#  Implementación de Merge Sort
def merge_sort(lista, clave):
    if len(lista) > 1:
        mid = len(lista) // 2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        merge_sort(izquierda, clave)
        merge_sort(derecha, clave)

        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i][clave] < derecha[j][clave]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
            
def quick_sort(lista, clave):
    if len(lista) <= 1:
        return lista[:]
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x[clave] < pivote[clave]]
    medio = [x for x in lista if x[clave] == pivote[clave]]
    derecha = [x for x in lista if x[clave] > pivote[clave]]
    return quick_sort(izquierda, clave) + medio + quick_sort(derecha, clave)

#  Implementación de Heap Sort
def heap_sort(lista, clave):
    heap = [(empleado[clave], empleado) for empleado in lista]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]
    
def buscar_empleado(criterio, valor):
    resultados = [e for e in empleados if e[criterio] == valor]
    return resultados

#  Menú interactivo
def menu():
    while True:
        print("\n--- BIENVENIDO ---")
        print("1. Ordenar empleados por edad ")
        print("2. Ordenar empleados por salario ")
        print("3. Ordenar empleado por nombre")
        print("4. Buscar empleado por salario o edad")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            heap_sort()
        
        elif opcion == "2":
            merge_sort()

        elif opcion == "3":
            quick_sort()

        elif opcion == "4":
            buscar_empleado()

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú interactivo
menu()

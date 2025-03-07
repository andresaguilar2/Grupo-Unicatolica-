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
        print("4. Buscar empleado por salario")
        print("5. Buscar empleado por nombre")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            empleados_ordenados = empleados.copy()
            merge_sort(empleados_ordenados, "edad")
            print("\nEmpleados ordenados por edad:")
            for emp in empleados_ordenados:
                print(emp)
        
        elif opcion == "2":
            empleados_ordenados = empleados.copy()
            merge_sort(empleados_ordenados, "salario")
            print("\nEmpleados ordenados por salario:")
            for emp in empleados_ordenados:
                print(emp)

        elif opcion == "3":
            empleados_ordenados = empleados.copy()
            merge_sort(empleados_ordenados, "nombre")
            print("\nEmpleados ordenados por nombre:")
            for emp in empleados_ordenados:
                print(emp)

        elif opcion == "4":
            salario = int(input("Ingrese el salario a buscar: "))
            resultados = buscar_empleado("salario", salario)
            if resultados:
                print("\nEmpleados con salario", salario, ":")
                for emp in resultados:
                    print(emp)
            else:
                print("No se encontraron empleados con ese salario.")

        elif opcion == "5":
            edad = int(input("Ingrese la edad a buscar: "))
            resultados = buscar_empleado("edad", edad)
            if resultados:
                print("\nEmpleados con edad", edad, ":")
                for emp in resultados:
                    print(emp)
            else:
                print("No se encontraron empleados con esa edad.")

        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el menú interactivo
menu()


def BubbleSort(array):
    N = len(array)
    i = 0
    while i < N - 1:
        J = 0
        while J < N - i - 1:
            if array[J]["code"] > array[J + 1]["code"]:
                temp = array[J]
                array[J] = array[J + 1]
                array[J + 1] = temp
            J += 1
        i += 1
    return array

estudiantes = [{"name": "camila","code": 2},
               {"name": "daniel","code": 4},
               {"name": "sofia","code": 3},
               {"name": "juan","code": 5},
               {"name": "valentina","code": 7},
               {"name": "carlos","code": 6},
               {"name": "isabella","code": 9},
               {"name": "andres","code": 8},
               {"name": "mariana","code": 1},
               {"name": "felipe","code": 10}]   


arreglo_ordenado = BubbleSort(estudiantes)
for i in arreglo_ordenado:
  print(i)

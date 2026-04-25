# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    #return "ANSWER HERE"  # Remove this line and implement
    lista_plana = []
    for fila in matrix:
        for elemento in fila:
            lista_plana.append(elemento)
    return lista_plana


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    #return "ANSWER HERE"  # Remove this line and implement
    resultados = []
    for fila in matrix:
        suma_fila = 0
        for numero in fila:
            suma_fila += numero
        resultados.append(suma_fila)
    return resultados


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    #return "ANSWER HERE"  # Remove this line and implement
    if not matrix:
        return []

    num_filas = len(matrix)
    num_cols = len(matrix[0])
    resultados = []

    for j in range(num_cols):
        suma_col = 0
        for i in range(num_filas):
            suma_col += matrix[i][j]
        resultados.append(suma_col)
    return resultados
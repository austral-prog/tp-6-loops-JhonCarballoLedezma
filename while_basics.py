# Replace the "ANSWER HERE" for your answer

def countdown(n):
    """
    Retorna una lista con la cuenta regresiva desde n hasta 0.
    Si n < 0, retorna una lista vacia.

    Ejemplo: countdown(5) -> [5, 4, 3, 2, 1, 0]
    Ejemplo: countdown(0) -> [0]
    Ejemplo: countdown(-1) -> []
    """
    #return "ANSWER HERE"  # Remove this line and implement
    resultado = []
    while n >= 0:
        resultado.append(n)
        n = n - 1
    return resultado


def double_until(limit):
    """
    Comenzando desde 1, va duplicando el valor y agrega cada uno
    a una lista mientras sea menor o igual a limit.
    Si limit < 1, retorna una lista vacia.

    Ejemplo: double_until(10) -> [1, 2, 4, 8]
    Ejemplo: double_until(1) -> [1]
    Ejemplo: double_until(0) -> []
    """
    #return "ANSWER HERE"  # Remove this line and implement
    if limit < 1 :
        return []
    resultado = []
    valor_actual = 1

    while valor_actual <= limit :
        resultado.append(valor_actual)
        valor_actual = valor_actual * 2
    return resultado
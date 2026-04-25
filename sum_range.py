# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """
    #return "ANSWER HERE"  # Remove this line and implement
    if n <= 0:
        return 0
    num = 0
    for i in range(1,n+1):
        num = num + i
    return num 

#sum_to_n()


def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """
    #return "ANSWER HERE"  # Remove this line and implement
    if n <= 0:
        return 0
    num = 0
    for i in range(1,n+1):
        if i % 2 == 0:    
            num = num + i
    return num
#sum_evens()


def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """
    #return "ANSWER HERE"  # Remove this line and implement
    if n <= 0:
        return 1
    num = 1
    for i in range(1,n+1):
        num = num * i
    return num
#factorial()

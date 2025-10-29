def suma(a: float, b: float) -> float:
    """
    Calcula la suma de dos números.

    Args:
        a (float): Primer número a sumar
        b (float): Segundo número a sumar

    Returns:
        float: Resultado de la suma a + b

    Examples:
        >>> suma(5, 3)
        8.0
        >>> suma(-1, 1)
        0.0
    """
    return float(a + b)


def es_par(n: int) -> bool:
    """
    Determina si un número es par.

    Args:
        n (int): Número a evaluar

    Returns:
        bool: True si el número es par, False si es impar

    Examples:
        >>> es_par(4)
        True
        >>> es_par(7)
        False
    """
    # Un número es par si el resto de dividirlo por 2 es 0
    return n % 2 == 0


if __name__ == "__main__":
    # Ejemplos de uso
    print(f"Suma de 5 + 3 = {suma(5, 3)}")
    print(f"¿El número 4 es par? {es_par(4)}")
    print(f"¿El número 7 es par? {es_par(7)}")

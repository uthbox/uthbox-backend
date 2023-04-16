import random


def generar_codigo():
    """
        DOCSTRING: Funcion responsable de la generacion del codigo de verificacion
    """
    return random.randint(100000, 999999)
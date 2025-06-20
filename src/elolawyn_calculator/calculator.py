PI: float = 3.141592653589793


class Calculator:
    def __init__(self):
        raise TypeError(
            "La clase Calculator no se puede instanciar. Usa sus métodos estáticos."
        )

    @staticmethod
    def add(a: int | float, b: int | float) -> int | float:
        return a + b

    @staticmethod
    def subtract(a: int | float, b: int | float) -> int | float:
        return a - b

    @staticmethod
    def multiply(a: int | float, b: int | float) -> int | float:
        return a * b

    @staticmethod
    def divide(a: int | float, b: int | float) -> int | float:
        if b == 0:
            raise ValueError("No se puede dividir por cero.")

        return a / b

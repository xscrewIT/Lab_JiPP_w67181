import numpy as np
from functools import reduce


def matrix_operations(matrix_list, operation):
    if operation not in ['+', '*']:
        raise ValueError("Dozwolone operacje: '+' (suma) lub '*' (iloczyn)")

    if operation == '+':
        operation_func = lambda x, y: x + y
    elif operation == '*':
        operation_func = lambda x, y: np.dot(x, y)

    result = reduce(operation_func, matrix_list)
    return result


A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.array([[9, 10], [11, 12]])

matrix_list = [A, B, C]

operation = input("Wybierz operację (+ dla sumy, * dla iloczynu): ").strip()

try:
    result = matrix_operations(matrix_list, operation)
    print(f"Wynik operacji {operation} na macierzach:\n{result}")
except ValueError as e:
    print(f"Błąd: {e}")

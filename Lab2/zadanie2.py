import numpy as np
import re

def validate_matrices(A, B, operation):
    if operation == "add":
        return A.shape == B.shape
    elif operation == "multiply":
        return A.shape[1] == B.shape[0]
    return True

def parse_and_execute(expression, matrices):
    add_pattern = re.compile(r"(\w+)\s*\+\s*(\w+)")
    multiply_pattern = re.compile(r"(\w+)\s*\*\s*(\w+)")
    transpose_pattern = re.compile(r"(\w+)\s*\.T")

    if match := add_pattern.match(expression):
        matrix1, matrix2 = match.groups()
        if matrix1 in matrices and matrix2 in matrices:
            A = matrices[matrix1]
            B = matrices[matrix2]
            if validate_matrices(A, B, "add"):
                return A + B
            else:
                raise ValueError("Wymiary macierzy są niezgodne do dodawania.")

    elif match := multiply_pattern.match(expression):
        matrix1, matrix2 = match.groups()
        if matrix1 in matrices and matrix2 in matrices:
            A = matrices[matrix1]
            B = matrices[matrix2]
            if validate_matrices(A, B, "multiply"):
                return A @ B
            else:
                raise ValueError("Wymiary macierzy są niezgodne do mnożenia.")

    elif match := transpose_pattern.match(expression):
        matrix1 = match.group(1)
        if matrix1 in matrices:
            A = matrices[matrix1]
            return A.T

    else:
        raise ValueError("Nieprawidłowa operacja.")

def matrix_operation_system(operations, matrices):
    for expression in operations:
        try:
            result = parse_and_execute(expression, matrices)
            print(f"Operacja '{expression}' zakończona wynikiem:\n{result}\n")
        except Exception as e:
            print(f"Błąd podczas wykonywania operacji '{expression}': {str(e)}")

matrices = {
    "A": np.array([[1, 2], [3, 4]]),
    "B": np.array([[5, 6], [7, 8]]),
    "C": np.array([[2], [3]])
}

operations = [
    "A + B",      # Dodawanie
    "A * B",      # Mnożenie
    "B * A",      # Mnożenie odwrotne
    "A.T",        # Transponowanie
    "A * C",      # Mnożenie z macierzą C
    "A + C"       # Niezgodne dodawanie
]

matrix_operation_system(operations, matrices)

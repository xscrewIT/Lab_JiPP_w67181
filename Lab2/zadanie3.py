def dynamic_data_analysis(data):
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    strings = list(filter(lambda x: isinstance(x, str), data))
    tuples = list(filter(lambda x: isinstance(x, tuple), data))

    max_number = max(numbers) if numbers else None

    longest_string = max(strings, key=len) if strings else None

    largest_tuple = max(tuples, key=len) if tuples else None

    return max_number, longest_string, largest_tuple


data = [
    3, 5, 10.2, "hello", "world",
    (1, 2), (1, 2, 3), {"key": "value"},
    [1, 2, 3], "a very long string", (1,)
]

max_number, longest_string, largest_tuple = dynamic_data_analysis(data)

print(f"Największa liczba: {max_number}")
print(f"Najdłuższy napis: {longest_string}")
print(f"Krotka o największej liczbie elementów: {largest_tuple}")

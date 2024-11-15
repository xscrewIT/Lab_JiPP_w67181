import ast


def generate_code(template, data):
    code = template.format(**data)

    try:
        ast.parse(code)
        print("Kod jest poprawny!")
    except SyntaxError as e:
        print(f"Błąd składni w kodzie: {e}")
        return None

    return code


def execute_code(code):
    if code:
        local_vars = {}
        try:
            exec(code, {}, local_vars)
        except Exception as e:
            print(f"Błąd wykonania kodu: {e}")
        return local_vars
    return None


template = """
def funkcja(x):
    return x + {addition_value}
"""

data = {
    "addition_value": 5
}

generated_code = generate_code(template, data)

local_vars = execute_code(generated_code)

if local_vars and 'funkcja' in local_vars:
    funkcja = local_vars['funkcja']
    result = funkcja(10)
    print(result)
else:
    print("Funkcja nie została poprawnie wygenerowana.")

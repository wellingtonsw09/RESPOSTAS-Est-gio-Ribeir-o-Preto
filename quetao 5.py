def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

# Exemplo de uso
string_original = "Olá, target sistemas"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
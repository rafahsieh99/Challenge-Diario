def invertir_caracteres(cadena_de_caracteres):
    if len(cadena_de_caracteres) == 0:
        return " "
    else:
        return cadena_de_caracteres[-1] + invertir_caracteres(cadena_de_caracteres[:-1])

palabra_usuario = input("Por favor, ingresa una palabra: ")

resultado = invertir_caracteres(palabra_usuario)
print(f"La palabra invertida es: {resultado}")
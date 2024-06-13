# Solicitar al usuario que ingrese una frase
frase = input('Ingrese un mensaje: ').lower()  # Convertir toda la frase a minúsculas

# Iniciar el contador de vocales
contador_vocales = 0

# Definir las vocales
vocales = "aeiou"

# Recorrer cada letra en la frase
for letra in frase:
    # Si la letra es una vocal
    if letra in vocales:
        print('Encontré una vocal:', letra)
        # Incrementar el contador de vocales
        contador_vocales += 1

# Mostrar el número total de vocales encontradas
print(f'El número total de vocales en la frase es: {contador_vocales}')


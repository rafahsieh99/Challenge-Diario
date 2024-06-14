def ordenar_lista(numeros):
    return sorted(numeros)

# Solicitar al usuario que ingrese una lista de números separados por comas
entrada = input('Ingrese una lista de números separados por comas: ')

# Convertir la cadena de entrada en una lista de números
numeros = [int(num) for num in entrada.split(',')]

# Ordenar la lista
lista_ordenada = ordenar_lista(numeros)

# Mostrar la lista ordenada
print('La lista ordenada es:', lista_ordenada)

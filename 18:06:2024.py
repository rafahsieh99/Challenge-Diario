# Función para convertir grados Celsius a grados Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicitar al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir la temperatura a grados Fahrenheit
fahrenheit = celsius_a_fahrenheit(celsius)

# Mostrar el resultado
print(f"{celsius} grados Celsius es igual a {fahrenheit} grados Fahrenheit.")

import random
import string

def generar_contraseña(longitud):
    if longitud < 8 or longitud > 16:
        return None  # Si la longitud no está dentro del rango permitido, devuelve None

    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def main():
    print("Generador de Contraseñas")
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña (8-16 caracteres): "))
            contraseña = generar_contraseña(longitud)
            if contraseña is None:
                print("Longitud inválida. Debe estar entre 8 y 16 caracteres.")
            else:
                print(f"Tu contraseña es: {contraseña}")

        except ValueError:
            print("Por favor, introduce un número válido.")
        
        respuesta = input("¿Generar otra contraseña? (sí/no): ").lower()
        if respuesta == "no":
            print("¡Gracias por usar el generador de contraseñas!")
            break

if __name__ == "__main__":
    main()

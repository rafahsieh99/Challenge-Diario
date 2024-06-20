import random

def computadora():
    elecciones = ["piedra", "papel", "tijera"]
    return random.choice(elecciones)

def usuario():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        print("Respuesta no valida intentalo de nuevo.")
        eleccion = input("Escoge piedra, papel o tijera: ").lower()
    return eleccion

def ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
        (usuario == "papel" and computadora == "piedra") or \
        (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

def jugar():
    print("Bienvenido al Hakembo")
    while True:
        eleccion_usuario = usuario()
        eleccion_computadora = computadora()
        print(f"La computadora eligio: {eleccion_computadora}")
        resultado = ganador(eleccion_usuario, eleccion_computadora)
        print(resultado)

        jugar_de_nuevo = input("¿Jugar de nuevo? (sí/no): ").lower()
        if jugar_de_nuevo == "no":
            print("Gracias por participar")
            break



# Ejecutar el juego
jugar()

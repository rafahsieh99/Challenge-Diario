#include <iostream>
#include <string>
#include <algorithm>

int main() {
    while (true) {
        int numero1, numero2;
        std::string respuesta;

        // Solicitar al usuario el primer número
        std::cout << "Ingrese su primer numero: ";
        std::cin >> numero1;

        // Solicitar al usuario el segundo número
        std::cout << "Ingrese su segundo numero: ";
        std::cin >> numero2;

        // Calcular y mostrar la suma de los dos números
        std::cout << "La suma de " << numero1 << " y " << numero2 << " es: " << numero1 + numero2 << std::endl;

        // Preguntar al usuario si quiere ingresar otros números
        std::cout << "¿Quieres ingresar otros números? (sí/no): ";
        std::cin >> respuesta;

        // Convertir la respuesta a minúsculas
        std::transform(respuesta.begin(), respuesta.end(), respuesta.begin(), ::tolower);

        if (respuesta == "no") {
            break;
        }
    }

    std::cout << "Hasta la proxima" << std::endl;
    return 0;
}

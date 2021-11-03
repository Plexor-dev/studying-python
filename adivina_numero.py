import random


def run():
    print("Bienvenido al juego de adivina el numero/n")
    numero_random = random.randint(1, 100)
    numero_usuario = int(input("Elige un numero del 1 al 100: "))
    while numero_usuario != numero_random:
        if numero_usuario < numero_random:
            print("El numero es mayor")
        else:
            print("El numero es menor")
        numero_usuario = int(input("Elige OTRO numero del 1 al 100: ")) #deben haber una separacion con el else en los espacios verticales para que no se confundan
    print("Felicidades, has adivinado el numero")


if __name__ == '__main__':
    run()
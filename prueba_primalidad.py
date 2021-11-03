def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    # contador = 0
    # for i in range(1, n+1):
    #     if i == 1 or i == n:
    #         continue
    #     if n % i == 0:
    #         contador += 1
    # if contador == 0:
    #     return True
    # else:
    #     return False


def run():
    numero = int(input("Ingrese un numero: "))
    if es_primo(numero):
        print("El numero es primo")
    else:
        print("El numero no es primo")


if __name__ == '__main__':
    run()
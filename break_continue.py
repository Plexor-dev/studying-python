def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    # texto = input("Escribe un texto: ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)
    # i = 0
    # while i != 10:
    #     if i == 5:
    #         i += 1
    #         continue
    #     print("Holaaa, esta es la vuelta " + str(i))
    #     i += 1


if __name__ == '__main__':
    run()
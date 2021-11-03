"""def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    # palabra_invertida = palabra[::-1]
    # if palabra == palabra_invertida:
    #     return True
    # else:
    #     return False
    return palabra == palabra[::-1] # esta forma es mas sencilla, se retorna True o False """

palindromo = lambda palabra: palabra == palabra[::-1]



def run():
    palabra = input("Ingrese una palabra: ").lower()
    es_palindromo = palindromo(palabra) # condicional ternario en una sola linea se escribe asi: palindromo(palabra) ? print("La palabra es palindroma") : print("La palabra no es palindroma")
    if es_palindromo:
        print(f"{palabra.capitalize()} es palindroma")
    else:
        print(f"{palabra.capitalize()} no es palindroma")


if __name__ == '__main__':
    run()
# print("el valor del dolar es de AR$185 = USD$1")

def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" + tipo_pesos + "tienes? ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """Bienvenido al conversor de monedas 💰
1. Pesos Colombianos
2. Pesos Argentinos 
3. Pesos Mexicanos

Elige una opción: """
opcion = int(input(menu)) # convierte el string a int y 

if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("argentinos", 185)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Elige una opción válida")


# convertir pesos argentinos a dolar
# convertir_dolar = input("Cuantos dolares tienes? ")
# convertir_dolar = float(convertir_dolar)
# valores_pesos = convertir_dolar * valor_dolar
# valores_pesos = round(valores_pesos, 2)
# valores_pesos = str(valores_pesos)
# print("Tienes $" + valores_pesos + " pesos")

# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a crear funciones!')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# def conversacion(mensaje):
#     print("Hola")
#     print("Como estas?")
#     print(mensaje)
#     print("Adios")

# opcion = int(input('Elige una opcion: (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opcion 1')
# elif opcion == 2:
#     conversacion('Elegiste la opcion 2')
# elif opcion == 3:
#     conversacion('Elegiste la opcion 3')
# else:
#     print('Opcion no valida')


def suma(a, b):
    print('Se suman 2 numeros')
    resultado = a + b
    return resultado

sumatoria = str(suma(1, 4))
print("El resultado es: " + sumatoria)
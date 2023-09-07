#  TUPLAS

def menu(): #procedimiento, ya que no retorna nada
    print("\nEscoje una opción")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Salir de aplicativo")
    
def validaOpcion(): #funcion, ya que retorna un valor
    try:
        opcion = int(input("Ingrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 5:
            return opcion
        else:
            print("La opción ingresada es incorrecta. Vuelva a intentarlo")
            return validaOpcion()
    except:
        print("Debe ingresar sólo números")
        return validaOpcion()

#1. Crear tupla con las vocales, mostrarla y decir cantidad de elementos y tipo de datos
def ejercicio1():
    vocales=("a", "e", "i", "o", "u")
    print(f"\nLas vocales son: {vocales}")
    print("Cantidad de elementos ", len(vocales))
    print("Tipo de datos: ", type(vocales))

#2. Crear tupla con los primeros 100 números naturales y mostrarla.
def ejercicio2():
    numeros = tuple(range(1,101))
    print(f"\nLos numeros del 1 al 100 son: {numeros}")

#3. Crear y mostrar tupla con los primeros 100 numeros impares
def ejercicio3():
    numerosimpares = ()
    for numero in range (1, 101, 2):
        numerosimpares += (numero,)
    
    print(numerosimpares)

#4.    
def ejercicio4():
    pass

#Controlador de ejercicios
while True:
    menu()
    opcion = validaOpcion()
    if opcion == 5:
        break
    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    else:
        ejercicio4()
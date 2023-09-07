#  LISTAS

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

#1. Lista con los primeros 100 números naturales y mostrar su contenido
def ejercicio1():
    numeros = list(range(1,101))
    print(f"\nEstos son los primeros cien números naturales:\n{numeros}")

#2. Lista con los primeros 100 números pares y mostrarsu contenido
def ejercicio2():
    numeros = list(range(101))
    i = 0
    numerospar= []
    for i in range(101):
        if numeros[i] % 2 == 0:
            numerospar.append(numeros[i])
    print(f"\nEstos son los primeros cien números pares:\n{numerospar}")

#3. Acepte 5 números por teclado y los almacene en una lista que luego los muestre en forma vertical
def validaEj3():
    try:
        numeros = []
        for i in range(5):
            opcion = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(opcion)
        return numeros
    except ValueError:
            print("Debe ingresar sólo números")
            return validaEj3()
    
def ejercicio3():
    numeros = validaEj3()
    print("\nLa lista de números creada por el usuario es: ")
    for i in range(5):
        print(numeros[i])

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
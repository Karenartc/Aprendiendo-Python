#  LISTAS

def menu(): 
    print("\nEscoje una opción")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Ejercicio 7")
    print("8. Ejercicio 8")
    print("9. Ejercicio 9")
    print("10. Ejercicio 10")
    print("11. Ejercicio 11")
    print("12. Ejercicio 12")
    print("13. Ejercicio 13")
    print("14. Ejercicio 14")
    print("15. Salir de aplicativo")

# 1. Lista con los primeros 100 números naturales y mostrar su contenido
def ejercicio1():
    numeros = list(range(1,101)) #Crea lista de números del 1 al 100
    print(f"\nEstos son los primeros cien números naturales:\n{numeros}")

# 2. Lista con los primeros 100 números pares y mostrarsu contenido
def ejercicio2():
    numeros = list(range(201)) #Crea lsita de 200 números
    i = 0
    numerospar= []
    for i in range(len(numeros)): #Por i en el rango del largo de la lista números
        if numeros[i] % 2 == 0: #Si el número en la posicion del valor de i divido entre 2 es 0
            numerospar.append(numeros[i]) #Agregar número en la posición del valor de i al la lista de numeros pares
    print(f"\nEstos son los primeros cien números pares:\n{numerospar}")

# 3. Acepte 5 números por teclado y los almacene en una lista que luego los muestre en forma vertical
def validaEj3():
    try:
        numeros = [] #Lista vacia
        for i in range(5): #Se realizará el ciclo 5 veces
            opcion = int(input(f"Ingrese el número {i+1}: ")) #Ingresa los números por teclado
            numeros.append(opcion) #Agrega el número ingresado a la lista
        return numeros #regresa la lista de números
    except ValueError:
            print("Debe ingresar sólo números")
            return validaEj3()
    
def ejercicio3():
    numeros = validaEj3() #Llama a la función
    print("\nLa lista de números creada por el usuario es: ")
    for i in range(5): #Se realizará el ciclo 5 veces
        print(numeros[i]) #Imprime el elemento que s eencuentre en la posicion que indique el valor de i

# 4. Crear y mostrar de forma vertical una lista de 5 palabras ingresadas por teclado.
def validaEj4():
    try:
        listaPalabra = []
        i = 1
        while i <= 5:
            palabra = input(f"Ingrese la palabra N°{i}: ")
            if palabra.isalpha():
                listaPalabra.append(palabra)
                i += 1
            else:
                print("Debe ingresar sólo palabras")
                validaEj4()
        return listaPalabra
    except Exception as e:
        print(f"Error: {e}")
        return validaEj4()  
    
def ejercicio4():
    palabras = validaEj4()
    print(f"\nLa lista ingresada por el usuario es: ")
    for i in range(5):
        print(palabras[i])

# 5. Realiza un programa que acepte un conjunto de números enteros ingresados por teclado.
#   para terminar el ingreso digita el -99. Mostrar el primer elemento, el último y la cantidad de elementos en la lista.
def validaEj5():
    try:
        print(f"\nIngrese el número (-99) para dejar de ingresar números")
        numero = 0
        listaNum = []
        i = 1
        while numero != -99:
            numero = int(input(f"Ingrese el número {i}: "))
            if numero != -99:
                listaNum.append(numero)
                i += 1
        return listaNum
    except ValueError:
        print("Debe ingresar un número entero")
        return validaEj5()

def ejercicio5():
    numeros = validaEj5()
    tamañoLista = len(numeros)
    print(f"El primer número ingresado es: {numeros[0]}")
    print(f"El primer último ingresado es: {numeros[tamañoLista-1]}")
    print(f"La cantidad de elementos en la lista es: {tamañoLista} \nSus elemento son: {numeros}")

# 6. Ingresar por teclado y almacenar un conjunto de palabras, termina el ingreso con la palabra stop.
#    Mostrar el primera palabra, último y la cantidad de palabras ingresadas.
def ejercicio6():
    pass

# 7. Ingresar por teclado y almacenar un conjunto de notas.
#    Mostrar las notas ingresadas y su promedio.
def ejercicio7():
    pass

# 8. Ingresar por teclado y almacenar un conjunto de notas.
#    Mostrar las notas ingresadas, la más alta y l más baja. Sin usar funciones.
def ejercicio8():
    pass

# 9. Ingresar por teclado y almacenar un conjunto de notas.
#    Mostrar la nota que indique el usuario según su posición. User primera posición es 1.
def ejercicio9():
    pass

# 10. Ingresar por teclado y almacenar números enteros. Mostrar el mayor y menos número
def ejercicio10():
    pass

# 11. Ingresar por teclado y almacenar números enteros en listas distintas a los positivos, negativos y ceros. Mostrar.
def ejercicio11():
    pass

# 12. Ingresar por teclado y almacenar números enteros en listas distintas a los pares e impares. Mostrar.
def ejercicio12():
    pass

# 13. Ingresar por teclado y almacenar números enteros, convestir su contenidoa números positivos. 
#     Mostrar la lista antes y después.
def ejercicio13():
    pass

# 14. Ingresar por teclado y almacenar números enteros, ordenar su contenido dejando en las primera posiciones los pares y en la súltimas los impares.
#     Mostrar la lista antes y después.
def ejercicio14():
    pass

#validador del ingreso en el controlador de ejercicios
def validaOpcion():
    try:
        opcion = int(input("Ingrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 15:
            return opcion
        else:
            print("La opción ingresada es incorrecta. Vuelva a intentarlo")
            return validaOpcion()
    except:
        print("Debe ingresar sólo números")
        return validaOpcion()

#Controlador de ejercicios
while True:
    menu()
    opcion = validaOpcion()
    if opcion == 15:
        break
    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    elif opcion == 4:
        ejercicio4()
    elif opcion == 5:
        ejercicio5()
    elif opcion == 6:
        ejercicio6()
    elif opcion == 7:
        ejercicio7()
    elif opcion == 8:
        ejercicio8()
    elif opcion == 9:
        ejercicio9()
    elif opcion == 10:
        ejercicio10()
    elif opcion == 11:
        ejercicio11()
    elif opcion == 12:
        ejercicio12()
    elif opcion == 13:
        ejercicio13()
    else:
        ejercicio14()
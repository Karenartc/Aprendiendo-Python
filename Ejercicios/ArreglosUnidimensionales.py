#  ARREGLOS UNIDIMENSIONALES

#importanción de libreria para utilizar los arreglos unidimensionales
import numpy as np

def menu():
    print("\nEscoje una opción")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Ejercicio 6")
    print("7. Salir de aplicativo")

#1. Crear arreglo con las vocales y mostrar arrego
def ejercicio1():   
    vocales = np.array(["a","e","i","o","u"])
    print(f"\nLas vocales son: \n{vocales}")

#2. Crear y mostrar los 100 primeros numeros naturales
def ejercicio2():
    numeros = np.arange(1,101)
    print(f"\nLos primeros cien números naturales son: \n{numeros}")

#3. Crear y mostrar los 100 primeros numeros pares
def ejercicio3():
    numerospar = np.arange(2, 202, 2)
    print(f"Los primeros cien números pares son: \n{numerospar}")

#4. Crear y mostrar los 100 primeros numeros impares
def ejercicio4():
    numerosimpar = np.arange(1, 202, 2)
    print(f"Los primeros cien números impares son: \n{numerosimpar}")

#5. Crear un arreglo con 10 números enteros ingresados por teclado. Debe mostar el primer y último número ingresado además de todo el arreglo.
def ejercicio5():
    try:
        numeros=[]
        for i in range(10):
            numero = int(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)
        numpyNum = np.array(numeros)
        print(f"El primer número ingresado es: {numpyNum[0]}")
        print(f"El último número ingresado es: {numpyNum[9]}")
        print(f"El arreglo de números es: {numpyNum}")
    except ValueError:
        print("Debe ingresar sólo números")
        ejercicio5()

#6. Crea un arreglo con 6 palabras ingresadas por teclado, mostrar el arreglo y la palabra con menor y mayor cantidad de caracteres.
def ejercicio6():
    try:
        palabras=[]
        i=0
        palabraMenor = "abcdefghijklmnopqrstuvwxyz"
        palabraMayor = ""
        while i < 6:
            palabra = input(f"Ingrese la palabra {i+1}: ")
            if palabra.isalpha():
                palabras.append(palabra)
                if len(palabra) < len(palabraMenor):
                    palabraMenor = palabra
                if len(palabra) > len(palabraMayor):
                    palabraMayor = palabra
                i+=1
        numpyPalabra = np.array(palabras)
        print(f"La palabra con menor cantidad de carácteres es: {palabraMenor}")
        print(f"La palabra con mayor cantidad de carácteres es: {palabraMayor}")
        print(f"El arreglo de palabras es: {numpyPalabra}")    
    except ValueError:
        print("Debe ingresar sólo palabras")
        ejercicio6()

#validador del ingreso en el controlador de ejercicios
def validaOpcion():
    try:
        opcion = int(input("Ingrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 7:
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
    if opcion == 7:
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
    else:
        ejercicio6()
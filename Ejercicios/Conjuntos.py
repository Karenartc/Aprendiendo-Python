#  CONJUNTOS

def menu(): 
    print("\nEscoje una opción")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Salir de aplicativo")

#1. Crear vonjunto con elementos enteros ingresados por teclado y mostrarlo
def ejercicio1():
    try:
        Conjunto=set()
        dato=1
        i=1
        while dato!=0:
            print("\nSi coloca 0 da el resultado")
            dato=int(input(f"Ingrese el número {i}: "))
            if dato != 0:
                Conjunto.add(dato)
                i += 1
        print(f"Elementos del Conjunto: {Conjunto}")
    except:
        print("Debe ingresar sólo números")
        return ejercicio1()


#2. Crear y mostrar conjunto con palabras ingresadas por teclado
def ejercicio2():
    try:
        conjunto = set()
        palabra="b"
        i=1
        while palabra != "z":
            print("\nSi coloca z muestra el resultado")
            palabra=input(f"Ingrese la palabra número {i}: ")       
            if palabra.isalpha:
                if palabra != "z":
                    conjunto.add(palabra)
                    i += 1
                else:
                    print("Se le mostrará el resultado")
            else:
                print("Debe ingresar sólo palabras")
                return ejercicio2()
        print(f"Elementos del Conjunto: {conjunto}")
    except:
        print("Debe ingresar sólo palabras")
        return ejercicio2()

#3. Crear y mostrar conjunto con notas ingresadas por teclado
def ejercicio3():
    try:
        controlador=int(input("\n¿Cuántas notas ingregará? "))
        i=0
        conjuntoNotas=set()
        while i < controlador:
            nota=float(input(f"Ingrese la nota {i+1}: "))
            if nota >= 0.0 and nota <= 7.0:
                conjuntoNotas.add(nota)
                i+=1
            else:
                print("La nota debe estar en el rando de 0.0 y 7.0")
        print(f"Las notas ingresadas son: {conjuntoNotas}")
    except ValueError:
        print("Debe ingresar sólo números")
        return ejercicio3()

#4.    
def ejercicio4():
    pass

#validador del ingreso en el controlador de ejercicios
def validaOpcion(): 
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
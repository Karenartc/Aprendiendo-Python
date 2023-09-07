def menu(): #Menu del aplicativo
    print("+" + "-" * 60 + "+")
    print("|" + " " *20 + " Menú Principal " + " " *24 + "|")
    print("|" + "-" * 60 + "|")
    print("|" + " " *12 + "1. Concatenación de dos números" + " " *17 + "|")
    print("|" + " " *12 +  "2. Separación de una cadena en dos" + " " *14 + "|")
    print("|" + " " *12 + "3. Salir de aplicativo" + " " *26 + "|")
    print("+" + "-" * 60 + "+")
    print(" ")

def validaOpcion(): #funcion que valida la opcion que ingresa en el menu
    try:
        opcion = int(input("Ingrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 3:
            return opcion
        else:
            print("La opción ingresada no está entre el rango de 1 a 3. Vuelva a intentarlo")
            return validaOpcion()
    except Exception:
        print("Debe ingresar sólo números")
        return validaOpcion()
    except KeyboardInterrupt:
        print("Usted no ingreso una palabra")
        return validaIngreso2()

def validaIngreso(cadena):
    try:
        n=int(input("ingrese el " + cadena + " numero: "))
        return n
    except ValueError:
        print("Usted no ingreso un valor numerico")
        return validaIngreso(cadena)
    except KeyboardInterrupt:
        print("Usted no ingreso un valor")
        return validaIngreso(cadena)
    
def validaIngreso1(): #funcion que valida el ingreso del valor del ejercicio 1
        n1 = validaIngreso("primer")
        n1 = str(n1)
        n2 = validaIngreso("segundo")
        n2 = str(n2)
        return n1 + n2

def ejercicio1() : #Permite el ingreso de dos números y luego los concatena
    print("+" + "-" * 60 + "+")
    print("|" + " " *12 + "1. Concatenación de dos números" + " " *17 + "|")
    print("+" + "-" * 60 + "+")
    print("La concatenacion de los dos numeros es igual a ", validaIngreso1())
    print(" ")

def validaIngreso2(): #funcion que valida el ingreso de valor del ejercicio 2
    try:
        palabra = input("Ingrese una palabra: ")
        solopalabra = palabra.isalpha()
        largoPalabra = len(palabra)
        if solopalabra == True:
            largoPalabra = len(palabra)
            if largoPalabra % 2 == 0:
                mitadPalabra = largoPalabra // 2
                mitad1= palabra[:mitadPalabra]
                mitad2=palabra[mitadPalabra:]
                print("El largo de la palabra ingresada es par, se separará a mitad:")
                return "La primera mitad es: " + mitad1 + ". Y la segunda mitad es: " + mitad2
            else:
                mitadPalabra = largoPalabra // 2
                mitad1= palabra[:mitadPalabra+1]
                mitad2=palabra[mitadPalabra+1:]
                print("El largo de la palabra ingresada es impar, se separará a mitad:")
                print("(Donde la primera mitad tiene una letra de más que la segunda)")
                return "La primera mitad es: " + mitad1 + ". Y la segunda mitad es: " + mitad2
        else:
            print("debe ingresar solo una palabra. Vuelva a intentarlo")
            return validaIngreso2()
    except KeyboardInterrupt:
        print("Usted no ingreso una palabra")
        return validaIngreso2()
    except:
        print("Usted no ingreso una palabra")
        return validaIngreso2()
    
def ejercicio2() : #Separación de una cadena en dos
    print("+" + "-" * 60 + "+")
    print("|" + " " *12 +  "2. Separación de una cadena en dos" + " " *14 + "|")
    print("+" + "-" * 60 + "+")
    print(" ")
    print(validaIngreso2()) 
    print(" ")
    
while True: #ciclo de control de aplicativo
    menu()
    opcion = validaOpcion()
    print(" ")
    if opcion == 3:
        print("+" + "-" * 60 + "+")
        print("|" + " " *12 + "3. Saliste del aplicativo" + " " *23 + "|")
        print("+" + "-" * 60 + "+")
        break
    else:
        if opcion == 1:
           ejercicio1()
        else:
            ejercicio2()

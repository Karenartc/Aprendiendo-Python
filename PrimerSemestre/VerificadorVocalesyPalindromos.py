def menu(): #Menu del aplicativo
    print("+" + "-" * 40 + "+")
    print("|" + " " *10 + " Menú Principal " + " " *14 + "|")
    print("|" + "-" * 40 + "|")
    print("|" + " " *10 + "1. Ejercicio 1" + " " *16 + "|")
    print("|" + " " *10 +  "2. Ejercicio 2" + " " *16 + "|")
    print("|" + " " *10 + "3. Salir de aplicativo" + " " *8 + "|")
    print("+" + "-" * 40 + "+")
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

def validaIngreso1(): #funcion que valida el ingreso de una letra en el ejercicio 1
    vocal = "aeiou"
    alfabeto = "bcdfghjklmnñpqrstvwxyz"
    try:
        letra = input("ingrese una letra: ").lower()
        if len(letra) == 1:
            if letra in vocal:
                return "una vocal"
            else:
                if letra in alfabeto:
                    return "una consonante"
                else:
                    print("Debe ingresar un letra. Vuelva a intentarlo")
                    return validaIngreso1()
        else:
            print("Ingreso más de una letra. Vuelva a intentarlo")
            return validaIngreso1()
    except Exception:
        print("Esto no es un valor válido")
        return validaIngreso1()

def ejercicio1() : #Pedir una letra e indicar si es vocal o consonante
    print("+" + "-" * 40 + "+")
    print("|" + " " *11 + " Ejercicio 1 " + " " *16 + "|")
    print("+" + "-" * 40 + "+")
    print("usted ha ingresado ", validaIngreso1())
    print(" ")

def validaIngreso2(): #funcion que valida el palindromo del ejercicio 2
    try:
        palabra = input("Ingrese una palabra: ")
        solopalabra = palabra.isalpha()
        if solopalabra == True:
            if palabra[::-1] == palabra:
                return "un palindromo"
            else:
                return "una palabra que NO es un palindromo"
        else:
            print("debe ingresar solo letras. Vuelva a intentarlo")
            return validaIngreso2()
    except:
        print("Ingreso un valor invalido")
        return validaIngreso2()
    
def ejercicio2() : #Determinar si una palabra ingresada por el usuario es palindroma.
    print("+" + "-" * 40 + "+")
    print("|" + " " *11 + " Ejercicio 2 " + " " *16 + "|")
    print("+" + "-" * 40 + "+")
    print(" ")
    print("usted ha ingresado ", validaIngreso2()) 
    print(" ")

while True: #ciclo de control de aplicativo
    menu()
    opcion = validaOpcion()
    print(" ")
    if opcion == 3:
        break
    else:
        if opcion == 1:
            ejercicio1()
        else:
            ejercicio2()

def menu(): #Menu del aplicativo
    print("+" + "-" * 60 + "+")
    print("|" + " " *20 + " Menú Principal " + " " *24 + "|")
    print("|" + "-" * 60 + "|")
    print("|" + " " *12 + "1. Combinación de palabras" + " " *22 + "|")
    print("|" + " " *12 +  "2. Contar vocal en texto ingresado" + " " *14 + "|")
    print("|" + " " *12 + "3. Salir de aplicativo" + " " *26 + "|")
    print("+" + "-" * 60 + "+")
    print(" ")

def validaOpcion(): #funcion que valida la opcion que ingresa en el menu
    try:
        opcion = int(input("Ingrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 3:
            return opcion
        else:
            print("OPCION NO VALIDA. La opción ingresada no está entre el rango de 1 a 3. Vuelva a intentarlo")
            return validaOpcion()
    except Exception:
        print("Debe ingresar sólo números")
        return validaOpcion()
    except KeyboardInterrupt:
        print("Usted no ingreso un valor")
        return validaOpcion()

def validaIngreso1(cadena): #valida el ingreso de lo requerido en ejercicio1
    try:
        palabra = input("ingrese la " + cadena + " palabra: ")
        soloPalabra = palabra.isalpha()
        if soloPalabra:
            return palabra
        else:
            print("Usted no ingreso una palabra")
            return validaIngreso1(cadena)
    except KeyboardInterrupt:
        print("Usted no esta ingresando lo indicado")
        return validaIngreso1(cadena)
    except:
        print("Usted no ingreso una palabra")
        return validaIngreso1(cadena)

def intercalar(cadena1, cadena2): #proceso de concatenacion de las letras de ambas palabras
    cadenaFinal = ""
    for i in range(len(cadena2)):
        cadenaFinal += cadena1[i] + cadena2[i]
        resto = len(cadena1) - len(cadena2)
    if resto:
        cadenaFinal += cadena1[-resto:]
    return cadenaFinal

def ejercicio1(): #proceso de la función combinar
    cadena1 = validaIngreso1("primera")
    largo1 = len(cadena1)
    cadena2 = validaIngreso1("segunda")
    largo2 = len(cadena2)
    if largo1 > largo2: #La cadena más grande es la que comienza el intercambio
        print("Se comenzara a intercalar con la palabra " + cadena1)
        return intercalar(cadena1, cadena2)
    else:
        if largo2 > largo1:
            print("Se comenzara a intercalar con la palabra " + cadena2)
            return intercalar(cadena2, cadena1)
        else:
            print("Se comenzara a intercalar con la palabra " + cadena1)
            return intercalar(cadena1, cadena2)
        
def combinar(): #intercala letras de dos palabras.
    print("+" + "-" * 60 + "+")
    print("|" + " " *12 + "1. Combinación de palabras" + " " *22 + "|")
    print("+" + "-" * 60 + "+")
    print("La combinación de las palabras ingresadas es: ", ejercicio1())
    print(" ")

def validaCadena(): #valida el ingreso de la cadena en el ejercicio2
    try:
        cadena = input("ingrese un texto: ").lower()
        if not cadena.isdigit(): 
            return cadena
        else:
            print("Usted no ingreso un texto")
            return validaCadena()
    except KeyboardInterrupt:
        print("Usted no esta ingresando lo indicado")
        return validaCadena()
    except:
        print("Usted no ingreso un texto")
        return validaCadena()

def validaVocal(): #valida el ingreso de la vocal en el ejercicio2
    try:
        vocales = "aeiou"
        vocal = input("ingrese una vocal: ").lower()
        if len(vocal) == 1:
            if vocal in vocales:
                return vocal
            else:
                print("Usted no igreso una vocal")
                return validaVocal()
        else:
            print("Usted no ingreso una vocal")
            return validaVocal()
    except KeyboardInterrupt:
        print("Usted no esta ingresando lo indicado")
        return validaVocal()
    except:
        print("Usted no ingreso una vocal")
        return validaVocal()
    
def ejercicio2(): #proceso de la función conteoVocal
    cadena = validaCadena()
    vocal = validaVocal()
    posicion = cadena.count(vocal)
    print("La vocal " + vocal + ", fue encontrada en ", posicion , " posicion(es)")
    

def conteoVocal(): #Contar vocal en texto ingresado.
    print("+" + "-" * 60 + "+")
    print("|" + " " *12 +  "2. Contar vocal en texto ingresado" + " " *14 + "|")
    print("+" + "-" * 60 + "+")
    ejercicio2()

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
            combinar()
        else:
            conteoVocal()

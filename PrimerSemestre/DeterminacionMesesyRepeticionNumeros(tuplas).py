import random
def menu(): #Menu del aplicativo
    print("\n+" + "-" * 60 + "+")
    print("|" + " Menú Principal ".center(60) + "|")
    print("|" + "-" * 60 + "|")
    print("|" + " " *16 + "1. ¿Que Mes es?" + " " *29 + "|")
    print("|" + "2. ¿Cuantas veces se repite?".center(60) + "|")
    print("|" + " " *16 + "3. Salir de aplicativo" + " " *22 + "|")
    print("+" + "-" * 60 + "+")

def validaOpcion(): #funcion que valida la opcion que ingresa en el menu
    try:
        opcion = int(input("\nIngrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 3:
            return opcion
        else:
            print("\nLa opción ingresada no está entre el rango de 1 a 3. Vuelva a intentarlo")
            return validaOpcion()
    except Exception:
        print("\nDebe ingresar sólo números")
        return validaOpcion()
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor")
        return validaOpcion()

def validaNumero(largoTupla):
    try:
        print("\nAhora debera escribir solo un numero")
        print("Si desea salir del ejercicio, ingrese el numero '0'\n")
        numero = int(input("¿Que numero desea ingresar? "))
        if numero >= 0 and numero <= largoTupla: 
            return int(numero)
        else:
            print(f"\nIngreso un numero fuera del rango, Ingrese un numero dentro del 1 y el {largoTupla}")
            return validaNumero(largoTupla)
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor")
        return validaNumero(largoTupla)
    except Exception:
        print("\nDebe ingresar sólo números")
        return validaNumero(largoTupla)

def meses(): #tupla meses del año, ingresar numero y mostrar el mes en esa posicion
    print("\n+" + "-" * 60 + "+")
    print("|" + " " *16 + "1. ¿Que Mes es?" + " " *29 + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "Ingrese un numero para saber a que mes del año corresponde".center(60) + "|")
    print("+" + "-" * 60 + "+")
    meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    numero = 1
    while numero != 0:
        largoTupla = len(meses)
        numero = validaNumero(largoTupla)
        if numero != 0:
            print("\n" + " " *5 + "+" + "-" * 50 + "+")
            print(" " *5 +  "|" + f"El numero {str(numero)} corresponde al mes {meses[numero-1]}".center(50) + "|")
            print(" " *5 + "+" + "-" * 50 + "+")    
    print("\n" + " " *5 + "+" + "-" * 50 + "+")
    print(" " *5 +  "|" + "Ingreso el numero 0 saldra del ejercicio".center(50) + "|")
    print(" " *5 + "+" + "-" * 50 + "+")

def validaNumero2():
    try:
        print("\nAhora debera escribir solo un numero")
        print("Nota: Puede ser un numero positivo o negativo\n")
        numero = int(input("¿Que numero desea ingresar? "))
        return int(numero)
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor")
        return validaNumero2()
    except Exception:
        print("\nDebe ingresar sólo números")
        return validaNumero2()

def aleatorio():
    i = 1
    listaNumeros = []
    #while i <= 15:
    numerosAleatorio = (random.randint(-1000, 1000))
    listaNumeros.append(numerosAleatorio)
    i += 1
    tupla = tuple(listaNumeros)
    return tupla
    
def numeros(): #tupla con N números, ingresar numero y determinar cuantas veces esta ese numero en la tupla.
    print("\n+" + "-" * 60 + "+")
    print("|" + "2. ¿Cuantas veces se repite?".center(60) + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "Determina cuantas veces se repite un numero en una tupla".center(60) + "|")
    print("+" + "-" * 60 + "+")
    tupla = aleatorio()
    numero = validaNumero2()
    print("\n" + " " *5 + "+" + "-" * 50 + "+")
    print(" " *5 + "|" + "En un tupla con 15 numeros aleatorios:".center(50) + "|")
    print(" " *5 + "+" + "-" * 50 + "+")
    print("\n",tupla)
    print("\n" + " " *5 + "+" + "-" * 50 + "+")
    print(" " *5 + "|" + f"El numero {numero} aparece {tupla.count(numero)} veces".center(50) + "|")
    print(" " *5 + "+" + "-" * 50 + "+")


while True: #ciclo de control de aplicativo
    menu()
    opcion = validaOpcion()
    if opcion == 3:
        print("\n+" + "-" * 60 + "+")
        print("|" + " " *16 + "3. Saliste del aplicativo" + " " *19 + "|")
        print("+" + "-" * 60 + "+")
        break
    else:
        if opcion == 1:
           meses()
        else:
            numeros()


def menu(): #Menu del aplicativo
    print("\n+" + "-" * 60 + "+")
    print("|" + " Menú Principal ".center(60) + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "1. ¿Dos listas son iguales?".center(60) + "|")
    print("|" + " " *16 +  "2. ¿Es palíndromo?" + " " *26 + "|")
    print("|" + " " *16 +  "3. Intercambiar elementos" + " " *19 + "|")
    print("|" + " " *16 + "4. Salir de aplicativo" + " " *22 + "|")
    print("+" + "-" * 60 + "+")

def validaOpcion(): #funcion que valida la opcion que ingresa en el menu
    try:
        opcion = int(input("\nIngrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 4:
            return opcion
        else:
            print("\nLa opción ingresada no está entre el rango de 1 a 4. Vuelva a intentarlo")
            return validaOpcion()
    except Exception:
        print("\nDebe ingresar sólo números")
        return validaOpcion()
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor")
        return validaOpcion()

def validaLista1(cadena, cantidad): #valida el ingreso de los elementos de la lista en ejercicio 1 y 3
    try:
        lista = []
        i = 1
        elemento = ""
        print(f"\nAhora ingresara los datos de la {cadena} lista (pueden ser numeros o palabras)")
        print("\n-" + "-" * 60 + "-")
        while i <= cantidad:
            elemento = input(" " * 16 + f"Ingrese el elemento N°{i}: ")
            lista.append(elemento)
            i += 1
        print("-" + "-" * 60 + "-")
        return lista
    except Exception:
        print("\nHa ingresado algo no indicado, vuelva a empezar")
        return validaLista1(cadena)
    except KeyboardInterrupt:
        print("\nNo ha ingresado lo indicado, vuelva a empezar")
        return validaLista1(cadena)
        
def listasIguales(): #Indicar si dos listas son iguales en contenido de elementos.
    try:
        print("\n+" + "-" * 60 + "+")
        print("|" + "1. ¿Dos listas son iguales?".center(60) + "|")
        print("|" + "-" * 60 + "|")
        print("|" + "Indica si el contenido en dos listas son iguales".center(60) + "|")
        print("+" + "-" * 60 + "+")
        cantidad = int(input("\nCuantos elementos desea ingresar? "))
        lista1 = validaLista1("primera", cantidad)
        lista2 = validaLista1("segunda", cantidad)
        if sorted(lista1) == sorted(lista2):
            print("\n+" + " " * 60 + "+")
            print("Ambas listas contienen los mismos elementos".center(60))
            print(f"La Primera lista {lista1}".center(60))
            print(f"La Segunda lista {lista2}".center(60))
            print("+" + " " * 60 + "+")
        else:
            print("\n+" + " " * 60 + "+")
            print("Ambas listas NO contienen los mismos elementos".center(60))
            print(f"La Primera lista {lista1}".center(60))
            print(f"La Segunda lista {lista2}".center(60))
            print("+" + " " * 60 + "+")
    except Exception:
        print("\nHa ingresado algo no indicado, vuelva a empezar")
        return listasIguales()
    except KeyboardInterrupt:
        print("\nNo ha ingresado lo indicado, vuelva a empezar")
        return listasIguales()
    
def validaListaString(): #valida el ingreso de los elementos de la lista en ejercicio 2
    try:
        lista = []
        i=1
        elemento = ""
        print(f"\nAhora ingresara los datos de la lista (Solo palabras)")
        print("Cuando desee dejar de ingresar elementos, escriba el numero '0'")
        #print("Nota: La diferencia en Mayusculas y Minusculas podria cambiar el resultado")
        print("\n-" + "-" * 60 + "-")
        while elemento != "0":
                elemento = input(" " * 16 + f"Ingrese la palabra N°{i}: ")
                if elemento != "0":
                    if elemento.isalpha():
                        lista.append(elemento)
                        i += 1
                    else:
                        print("\nNo ingreso una palabra, vuelva a intentarlo\n")
        print("-" + "-" * 60 + "-")
        print("\nIngreso el numero 0, continuaremos con la siguiente parte del ejercicio")
        return lista
    except Exception:
        print("\nHa ingresado algo no indicado, vuelva a empezar")
        return validaListaString()
    except KeyboardInterrupt:
        print("\nNo ha ingresado lo indicado, vuelva a empezar")
        return validaListaString()
    
def palindromo(): #lista de palabras, el usuario decide cuando dejar de ingresar, mostrar cuales son palíndromo.
    print("\n+" + "-" * 60 + "+")
    print("|" + " " *16 +  "2. ¿Es palíndromo?" + " " *26 + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "Indica que palabras ingresadas son palíndromo".center(60) + "|")
    print("+" + "-" * 60 + "+")
    listapalindromo = []
    sipalindromo = 0
    lista = validaListaString()
    for palabra in lista:
        if palabra[::-1] == palabra:
            listapalindromo.append(palabra)
            sipalindromo += 1
    if sipalindromo > 0:
        print("\n+" + " " * 60 + "+")
        print(f"Hemos encontrado {sipalindromo} palabra(s) palindroma(s)".center(60))
        print(f"Las palabras ingresadas fueron: {lista}".center(60))
        print(f"Las palabras palindromos son: {listapalindromo}".center(60))
        print("+" + " " * 60 + "+")
    else:
        print("\n+" + " " * 60 + "+")
        print(f"Hemos encontrado 0 palabra(s) palindroma(s)".center(60))
        print(f"Las palabras ingresadas fueron: {lista}".center(60))
        print("+" + " " * 60 + "+")

def validaLista2(): #valida el ingreso de los elementos de la lista en ejercicio 3
    try:
        lista = []
        i=1
        elemento = ""
        print(f"\nAhora ingresara los datos de la lista (pueden ser numeros o palabras)")
        print("Cuando desee dejar de ingresar elementos, escriba el numero '0'")
        print("\n-" + "-" * 60 + "-")
        while elemento != "0":
                elemento = input(" " * 16 + f"Ingrese el elemento N°{i}: ")
                if elemento != "0":
                    lista.append(elemento)
                i += 1
        print("-" + "-" * 60 + "-")
        print("\nIngreso el numero 0, continuaremos con la siguiente parte del ejercicio")
        return lista
    except Exception:
        print("\nHa ingresado algo no indicado, vuelva a empezar")
        return validaLista2()
    except KeyboardInterrupt:
        print("\nNo ha ingresado lo indicado, vuelva a empezar")
        return validaLista2()

def intercambiar(): #Intercambiar todos los elementos de una lista de extremo a extremo.
    print("\n+" + "-" * 60 + "+")
    print("|" + " " *16 +  "3. Intercambiar elementos" + " " *19 + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "Intercambia los elementos de una lista".center(60) + "|")
    print("+" + "-" * 60 + "+")
    lista = validaLista2()
    print("\n+" + " " * 60 + "+")
    print(f"Los elementos ingresados son: ".center(60))
    print(str(lista).center(60))
    lista.reverse()
    print(f"Los elementos intercambiados son: ".center(60))
    print(str(lista).center(60))
    print("+" + " " * 60 + "+")

while True: #ciclo de control de aplicativo
    menu()
    opcion = validaOpcion()
    if opcion == 4:
        print("\n+" + "-" * 60 + "+")
        print("|" + " " *16 + "4. Saliste del aplicativo" + " " *19 + "|")
        print("+" + "-" * 60 + "+")
        break
    else:
        if opcion == 1:
           listasIguales()
        else:
            if opcion == 2:
                palindromo()
            else:
                intercambiar()

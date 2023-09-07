def menu(): #Menu del aplicativo
    print("\n+" + "-" * 60 + "+")
    print("|" + " Menú Principal ".center(60) + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "1. Contactos".center(60) + "|")
    print("|" + "2. Productos".center(60) + "|")
    print("|" + " " *24 + "3. Salir de aplicativo" + " " *14 + "|")
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
    
def desicion(cadena): #cotrola el ingreso de productos/conatctos en ambos ejercicios
    try:
        pregunta=input(f"¿Desea ingresar un {cadena}? (responder con S/N): ")
        pregunta=pregunta.lower()
        if pregunta.isalpha():
            if pregunta=="s" or pregunta=="n":
                return pregunta
            else:
                print("\nRespuesta invalida. Debe ingresar 'S' o 'N'")
                return desicion(cadena)
        else:
            print("\nSolo se permiten palabras, vuelva a intentarlo.")
            return desicion(cadena)
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor, vuelva a intentarlo.")
        return desicion(cadena)
    except:
        print("\nError, vuelva a intentarlo.")
        return desicion(cadena)

def ingresoPalabra(cadena): #es llamado en ambos ejercicios, valida ingreso de palabras
    try:
        dato=input(f"Ingrese {cadena}: ".center(45))
        dato2=dato.replace(" ","")
        if dato2.isalpha():
            return dato
        else:
            print("Debe ingresar sólo palabras")
            return ingresoPalabra(cadena)
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor, vuelva a intentarlo.")
        return ingresoPalabra(cadena)
    except:
        print("\nError, vuelva a intentarlo.")
        return ingresoPalabra(cadena)

def ingresoTelefono(): #llamado en ejercicio 2 y valida el ingreso de al menos 8 numeros
    try:
        telefono=input("Introduce el número de teléfono: ".center(45))
        if telefono.isdigit():
            if len(telefono) >= 8:
                return telefono
            else:
                print("Debe ingresar al menos 8 números. Vuelva a intentarlo.")
                return ingresoTelefono()
        else:
            print("Debe ingresar sólo números. Vuelva  a intentarlo.")
            return ingresoTelefono()
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor")
        return ingresoTelefono()
    except:
        print("\nError, vuelva a intentarlo.")
        return ingresoTelefono()

def contactos(): #clave(nombre): valor(teléfono). Mostrar la lista de contactos.
    print("\n+" + "-" * 60 + "+")
    print("|" + "1. Contactos".center(60) + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "Muestra diccinario de contactos (nombre y telefono)".center(60) + "|")
    print("+" + "-" * 60 + "+")
    try:
        agenda = {}
        while True:
            pregunta=desicion("contacto")
            if pregunta=="s":
                print("\n+" + " " * 60 + "+")
                nombre=ingresoPalabra("Nombre y Apellido")
                telefono=ingresoTelefono()
                print("+" + " " * 60 + "+")
                if(nombre not in agenda):
                    agenda[nombre] = telefono
                    print("\n" + " "*10 + "+" + "-" * 30 + "+")
                    print(" "*10 + "|" + 'Añadido el contacto'.center(30) + "|")
                    print(" "*10 + "+" + "-" * 30 + "+\n")
                else:
                    print('Ingreso un nombre de un contacto ya guardado\n'.center(40))
            else:
                print("\n+" + "-" * 60 + "+")
                print("|" + "Los contactos agendados son:".center(60) + "|")
                print("+" + "-" * 60 + "+")
                print(f"{agenda}".center(60))
                break
    except KeyboardInterrupt:
        print ("Usted no ingreso un valor, vuelva a intentarlo.")
        return contactos()
    except Exception:
        print ("Error, vuelva a intentarlo..")
        return contactos()

def ingresoNumero(cadena): #valida el ingreso de solo numeros
    try:
        numero=int(input(f"Ingrese {cadena} (sólo números): ".center(45)))
        return numero
    except ValueError:
        print("\nDebe ingresar solo numeros enteros, vuelva a intentarlo.")
        return ingresoNumero(cadena)
    except KeyboardInterrupt:
        print("\nUsted no ingreso un valor, vuelva a intentarlo.")
        return ingresoNumero(cadena)
    except:
        print("\nError, vuelva a intentarlo")
        return ingresoNumero(cadena)


    
def mostrarMayor(opcion, lista2): 
    listaMayor=[]
    for i in range(len(lista2)):
        if i ==0:
            listaMayor.append((lista2[0][0], lista2[0][opcion]))
        else:
            if listaMayor[0][1] < lista2[i][opcion]:
                listaMayor = []
                listaMayor.append((lista2[i][0], lista2[i][opcion]))
            elif listaMayor[0][1]==lista2[i][opcion]:
                 listaMayor.append((lista2[i][0], lista2[i][opcion]))   
    if len(listaMayor) >0:
        if opcion==1:
            cadena ="precio"
        else:
            cadena = "stock"
        print(" "*12 + "+" + "-" * 50 + "+")
        print(" "*12 + "|" + f"Productos con mayor {cadena}".center(50) + "|")
        print(" "*12 + "|" + "-" * 50 + "|")
        for i in range(len(listaMayor)):
            print(" "*12 + "|" + f"{listaMayor[i][0]} con un {cadena} de {listaMayor[i][1]}".center(50) + "|")
            print(" "*12 + "+" + "-" * 50 + "+")
            
            

def productos():#clave(código)asociado, nombre, precio, stock. Mostrar productos, el mas caro y el mayor stock.
    print("\n+" + "-" * 60 + "+")
    print("|" + "1. Productos".center(60) + "|")
    print("|" + "-" * 60 + "|")
    print("|" + "Muestra diccionario de productos".center(60) + "|")
    print("|" + "(codigo, nombre, precio y stock)".center(60) + "|")
    print("|" + "El producto mas caro y el que tiene mas stock".center(60) + "|")
    print("+" + "-" * 60 + "+")
    diccionario={}
    lista1 = []
    lista2 = []  
    while True:
        pregunta=desicion("producto")
        if pregunta=="s":
            print("\n+" + " " * 60 + "+")
            codigo=ingresoNumero("codigo")
            nombre=ingresoPalabra("Nombre")
            lista1.append(nombre)
            precio=ingresoNumero("precio")
            lista1.append(precio)
            stock=ingresoNumero("stock")
            print("+" + " " * 60 + "+")
            lista1.append(stock)
            diccionario[codigo]= lista1
            lista1=[]
        if pregunta=="n":
            lista2=list(diccionario.values())
            print("+" + "-" * 70 + "+")
            print("|" + "En el diccionario:".center(70) + "|")
            print("+" + "-" * 70 + "+")
            print(f"{diccionario}".center(70) + "\n")
            mostrarMayor(1, lista2)
            mostrarMayor(2, lista2)
            break

while True: #ciclo de control de aplicativo
    menu()
    opcion = validaOpcion()
    if opcion == 3:
        print("\n+" + "-" * 60 + "+")
        print("|" + "3. Saliste del aplicativo".center(60) + "|")
        print("+" + "-" * 60 + "+")
        break
    else:
        if opcion == 1:
           contactos()
        else:
            productos()

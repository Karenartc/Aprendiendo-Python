#  DICCIONARIOS

def menu(): #procedimiento, ya que no retorna nada
    print("\nEscoje una opción")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("4. Ejercicio 4")
    print("5. Ejercicio 5")
    print("6. Salir de aplicativo")
    
def validaOpcion(): #funcion, ya que retorna un valor
    try:
        opcion = int(input("Ingrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("La opción ingresada es incorrecta. Vuelva a intentarlo")
            return validaOpcion()
    except:
        print("Debe ingresar sólo números")
        return validaOpcion()

#1. Crear un diccionario con los datos de una persona y mostrarlo: nombre, direccion, edad y teléfono
def ejercicio1():
    datosPersona = {
    "Nombre": "Lola",
    "Direccion": "Calle123",
    "Edad": 23,
    "Teléfono": 89674523
    }

    print(f"\nLos datos de la persona son: {datosPersona}")

#2. Crear diccionario con los datos de un artículo ingresados por teclado y luego mostrarlo: código, nombre, precio, stock
def ejercicio2():
    try:
        articulos={
                    "codigo":0,
                    "nombre":"",
                    "precio":0.0,
                    "stock":1
                    }
        
        codigoArt=int(input("\nIngrese el código del artículo (sólo números): "))
        articulos["codigo"]=codigoArt

        nombreArt = input("Ingrese el nombre del artículo: ")
        if not nombreArt.isalpha():
            print("Debe ingresar solo letras como nombre del artículo.")
            return ejercicio2()
        articulos["nombre"]=nombreArt
            
        precioArt=float(input("Ingrese el precio del artículo (sólo números): "))
        articulos["precio"]=precioArt
        
        print("Ingrese 1 si está en stock \nIngrese 0 si no está en stock")
        stockArt=int(input("Ingrese el stock del artículo: "))
        if stockArt not in [0, 1]:
            print("Debe ingresar solo número 1 o 0 como stock del artículo.")
            return ejercicio2()
        articulos["stock"]=stockArt
            
        print(f"El artículo es:\n{articulos}")
        
    except ValueError:
        print("Error, vuelva a intentarlo")
        return ejercicio2()

#3. Crear diccionario que convierta un número entre 1 y 10 en su equivalente en palabra. Ej: 4->Cuatro    
def ejercicio3():
    palabraNumero={
        1:"Uno",
        2:"Dos",
        3:"Tres",
        4:"Cuatro",
        5:"Cinco",
        6:"Seis",
        7:"Siete",
        8:"Ocho",
        9:"Nueve",
        10:"Diez"
    }
    

#4.    
def ejercicio4():
    pass

#5.    
def ejercicio5():
    pass

#Controlador de ejercicios
while True:
    menu()
    opcion = validaOpcion()
    if opcion == 6:
        break
    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    elif opcion == 4:
        ejercicio4()
    else:
        ejercicio5()
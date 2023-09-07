def menu(): #procedimiento, ya que no retorna nada
    print("Menú Principal")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Salir de aplicativo")
    
def validaOpcion(): #funcion, ya que retorna un valor
    try:
        opcion = int(input("Ingrese opción a ejecutar: "))
        if opcion >= 1 and opcion <= 3:
            return opcion
        else:
            print("La opción ingresada es incorrecta. Vuelva a intentarlo")
            return validaOpcion()
    except:
        print("Debe ingresar sólo números")
        return validaOpcion()

def validaNumero():
    try:
        numero=int(input("Ingrese el numero:"))
        return  numero
    except:
        print("Debe ingresar sólo números enteros")
        return validaNumero()
    
def ejercicio1(): #Ejercio 1 que imprime las cantidades de numeros ingresados de pendiendo de los requisitos
    x = 1
    cont10y90 = 0
    contNeg10 = 0
    nocumple = 0
    print("A continuación deberá ingresar 4 números")
    while x <=4:
        print("Numero #", x)
        numero=validaNumero()
        if numero>10 and numero<90:
            cont10y90 = cont10y90+1
        elif numero<-10:
            contNeg10 = contNeg10+1
        else:
            nocumple = nocumple+1
        x = x+1
    print("La cantidad de números ingresados mayores a 10 y menores a 90 es: ",cont10y90)
    print("La cantidad de números ingresados menores a -10 es: ",contNeg10)
    print("La cantidad de números ingresados que no cumplen con las condiciones antertiores son: ",nocumple)
    tecla = input("Digite cualquier letra para continuar: ")

def validaSueldo():
    try:
        Sueldo=int(input("Ingrese sueldo del empleado: "))
        return  Sueldo
    except:
        print("Debe ingresar un sueldo mayor a cero")
        return validaSueldo()

def validaBono():
    try:
        Bono=int(input("Ingrese el bono del empleado: "))
        if Bono >= 0:
            return  Bono
    except:
        print("Debe ingresar un bono mayor a cero")
        return validaBono()

def ejercicio2(): #Ejercicio 2 que imprime porcentajes, promedios y cantidades dependiendo de los requisitos de los datos ingresados
    contadorBono = 0
    x = 1
    sueldoBono = 0
    contadorBono = 0
    sumaBono=0
    print("Ingrese datos de los 5 empleados")
    while x<= 5:
        print("Empleado #",x)
        Sueldo=validaSueldo()
        Bono= validaBono()
        sumaBono = Bono+sumaBono
        if Bono==40000:
            contadorBono = contadorBono+1
        if Sueldo>1800000:
            if Bono>=20000 and Bono<=25000:
                sueldoBono=sueldoBono+1
        x=x+1
    porcentajeBono = round((contadorBono*100)/5)
    promedioBono = round(sumaBono/5)
    print("El porcentaje de personas que recibieron un bono de $40000 es de ",porcentajeBono,"%")
    print("La cantidad de empleados con sueldo superior a $1800000 y el bono recibido se encuentra entre $20000 y $25000 es de ",sueldoBono)
    print("El promedio de los bonos recibidos por los empleados de la empresa es de $",promedioBono)
    tecla = input("Digite cualquier letra para continuar: ")

#ciclo de control de aplicativo
while True:
    menu()
    opcion = validaOpcion()
    if opcion == 3:
        break
    if opcion == 1:
        ejercicio1()
    else:
        ejercicio2()
        

x = 1
sumBono = 0
cantBono = 0
bono40 = 0
cantEmpleado = 0
promBono = 0
print("Bienvenido a la Empresa Apretados S.A")
while x<=2:
    print("Va a ingresar los datos del empleado n.",x)
    nombre = input("Ingrese su nombre: ")
    print("¿Cuál es su sueldo?")
    sueldo = int(input(" "))
    if sueldo > 0:
        print("¿Recibió algún bono? Si es asi ¿De cuánto?")
        print("Si no recibió un bono coloque un 0")
        bono = int(input(" "))
        if bono >= 0:
            x = x + 1
            if bono > 0:
                sumBono = sumBono + bono
                cantBono = cantBono + 1
                if bono == 40000:
                    bono40 = bono40 + 1
                    print("t",cantEmpleado)
                if sueldo > 1800000:
                    print("t",cantEmpleado)
                    if bono >= 20000 and bono <= 25000:
                        cantEmpleado = cantEmpleado + 1
                        print("t",cantEmpleado)
            else:
                print(nombre," no recibió bono")
        else:
            print(nombre," ingresó un bono que no corresponde")   
    else:
        print(nombre," ingresó un sueldo que no corresponde")
if cantBono > 0:
    porBono40 = (bono40*100)/cantBono
    promBono = sumBono / cantBono
    print("El porcentaje de empleados que recibieron un bono de 40000 mil pesos es: ", porBono40 ,"%")
    print("La cantidad de empleados con un sueldo superior a 1800000 mil pesos y que recibieron un bono entre los 20000 y los 25000 mil pesos son: ", cantEmpleado)
    print("El promedio de bonos recibidos por los empleados de la empresa es de: ",promBono)
else:
    print("Ningun empleado recibio un bono")

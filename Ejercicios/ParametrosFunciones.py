#1

def suma(dato, cantidad):
    sumatotal = 0
    i = 0
    for i in range(cantidad):
        sumatotal += dato[i]
    return sumatotal

def promedio(dato, cantidad):
    sumanum = suma(dato, cantidad)
    promedio = sumanum / cantidad
    return promedio
   

cantidad = input("¿Cuántos datos ingresará? ")
cantidad = int(cantidad)
i = 0
numeros = []

for i in range(cantidad):
    dato = input(f"Ingrese el número {i+1}: ")
    dato = int(dato)
    numeros.append(dato)
   
print(f"La suma de los números ingresados: {numeros} es: {suma(numeros, cantidad)}")
print(f"El promedio de los números ingresados: {numeros} es: {promedio(numeros, cantidad)}")

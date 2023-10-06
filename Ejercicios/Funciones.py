#1
def invMult(x):
    if x != 0:
        print("Inverso multiplicativo: ", 1/x)
    else:
        print("No existe Inverso multiplicativo ")

num = 5
invMult(num)

#2
def invAd(x):
    return -x

nume=5
print("El inverso aditivo de",nume, "es:", invAd(nume))

#3
def suma(x,y):
    return(x+y)

num1=5
num2=90
print(f"La suma de {num1} y {num2} es: {suma(num1,num2)}")

#4
def mayor2(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "Ninguno. Son iguales"

numero1=9
numero2=8
print(f"De los numeros ingresado {numero1, numero2}. El mayor es {mayor2(numero1, numero2)}")

#5
def mayor3(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return "Ninguno. Hay numeros iguales"

nume1=8
nume2=9
nume3=10
print(f"De los numeros ingresado {nume1, nume2, nume3}. El mayor es {mayor3(nume1, nume2, nume3)}")

#6
def parImpar(x):
    if x % 2 == 0:
        print(f"El número {x} es par")
    else:
        print(f"El número {x} es impar")

parImpar(-4)

#7
def multiplo(x,y):
    if y % x == 0:
        print(f"{y} es múltiplo de {x}")
    else:
        print(f"{y} no es múltiplo de {x}")

multiplo(7 , 21)

#8
def determinar(x):
    if x == 0:
        print(f"0. El número es neutro")
    elif x > 0:
        print(f"1. El número es positivo")
    else:
        print(f"-1. El número es negativo")

determinar(-5)

#9 Lo mismo que el 6

#10
def valorAbsoluto(x):
    if x < 0:
        return x*-1
    else:
        return x
   
valor = -10
print(f"El valor absoluto de |{valor}| es: {valorAbsoluto(valor)}")

#11

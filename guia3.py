"""
1. Escribí un programa que le solicite al usuario un número entero y
muestre todos los números correlativos entre el 1 y el número ingresado
por el usuario.
"""

print("Ingrese un numero entero")
num= int(input())
cont = 1

for i in range(0, num): 
    if num > cont:
        print(cont)
        cont = cont + 1
    elif num == cont:
        print(num)

"""
2.Imprimir los número del 0 al 9.        
"""

cont = 0
max = 9

for i in range(0, max + 1):
    if cont < max:
        print(cont)
        cont = cont + 1
    else:
        print(max)

"""
3. Pedir ingresar una frase e imprimir sus caracteres.
"""

print("Ingrese una frase")
frase = str(input())


for i in frase:
    print(i)
    
"""
4. Escribí un programa que, dado un número por el usuario, muestre todos
sus divisores positivos. Recordá que un divisor es aquel que divide al
número de forma exacta (con resto 0).
"""

print("Ingrese un numero")
num = int(input())

for i in range (1, num + 1):
    if num % i == 0:
        print(i)

"""
5. Escribí un programa que permita al usuario ingresar 6 números enteros,
que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de
los números negativos y el promedio de los positivos. No olvides que no
es posible dividir por cero, por lo que es necesario evitar que el programa
arroje un error si no se ingresaron números positivos.
"""


print("Ingrese un numero entero")
num = int(input())
neg = 0
pos = 0
contP = 0

for i in range (0,5):
    if num > 0:
        pos = pos + num
        contP = contP + 1
        print("Ingrese un numero")
        num = int(input())
    if num < 0:
        neg = neg + num
        print("Ingrese un numero")
        num = int(input())

if contP == 0:
    print("Los suma de negativos es", neg )
    print("No es posible dividir por 0")
else: 
     print("Los suma de negativos es", neg )
     print("El promedio de los positivos es", pos / contP)

"""     
6. Escribí un programa que, dada una frase por el usuario, la muestre
invertida.
"""


print("Ingrese una frase")
frase = str(input())
letra= len(frase)

for i in frase:
    if letra > 0:
        print(frase[letra-1])
        letra = letra - 1

"""
7. Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números ingresados.       
"""

print("Ingrese un numero")
num = int(input())
cont = 0

while num != 0:
    cont = cont + num 
    print("Ingrese un numero")
    num = int(input())

    if num == 0:
        break

print("la suma de los numeros ingresados es", cont)

"""
8. Leer números enteros de teclado, hasta que el usuario ingrese el 0.
Finalmente, mostrar la sumatoria de todos los números positivos
ingresados.
"""

print("Ingrese un numero")
num = int(input())
cont = 0

while num != 0:
    if num % 2 == 0:
        cont = cont + num 
        print("Ingrese un numero")
        num = int(input())
    if num % 2 == 1:
        print("Ingrese un numero")
        num = int(input())
    if num == 0:
        break
   

print("la suma de los numeros ingresados es", cont)

"""
9. Leer números enteros positivos de teclado, hasta que el usuario ingrese
el 0. Informar cuál fue el mayor número ingresado.
"""

print("Ingrese un numero")
num = int(input())
mayor = 0

while num != 0:
    if num > mayor:
        mayor = num
        print("Ingrese un numero")
        num = int(input())
    if num < mayor:
        print("Ingrese un numero")
        num = int(input())
    if num == 0:
        break

print("El numero mas grande es ", mayor)

"""
10.Leer un número entero positivo desde teclado e imprimir la suma de los
dígitos que lo componen.
"""

print("Ingresar un numero de dos digitos")
num = int(input())
suma = 0

num1 = num//10
num2 = num % 10
suma = num1 + num2
print("La suma de los digitos es ", suma)

"""
11.Solicitar al usuario que ingrese números enteros positivos y, por cada
uno, imprimir la suma de los dígitos que lo componen. La condición de
corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los
números ingresados por el usuario fueron números pares.
"""


print("Ingrese un numero entero positivo")
num= int(input())

cont = 0

while True:
    if num == -1:
        break
    if num % 2 == 0:
        cont = cont + 1
        num1 = num//10
        num2 = num % 10
        suma = num1 + num2
        print("La suma de los digitos que lo componen es ", suma)
        print("Ingrese un numero")
        num = int(input())
    else:
        num1 = num//10
        num2 = num % 10
        suma = num1 + num2
        print("Ingrese un numero")
        num = int(input())

print("La cantidad de numeros pares es ", cont)

"""
12.Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir
listado, 3-finalizar programa. A continuación, el usuario debe poder
seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta,
informarle del error. El menú se debe volver a mostrar luego de ejecutada
cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se
imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del
menú y el programa finalizará.
"""

print("1: Iniciar programa, 2: Imprimir listado, 3: finalizar programa")
opcion = int(input())

while True:
    if opcion == 1:
        print("Inicializando programa")
        print("1: Iniciar programa, 2: Imprimir listado, 3: finalizar programa")
        opcion = int(input())
    if opcion == 2:
        print("Imprimiendo Listado...")
        print("1: Iniciar programa, 2: Imprimir listado, 3: finalizar programa")
        opcion = int(input())
    if opcion == 3:
        break
    if opcion != 1 or opcion != 2 or opcion != 3:
        print("Opcion no valida ")
        print("1: Iniciar programa, 2: Imprimir listado, 3: finalizar programa")
        opcion = int(input())

"""
13.Solicitar al usuario el ingreso de una frase y de una letra (que puede o no
estar en la frase). Recorrer la frase, carácter a carácter, comparando con
la letra buscada. Si el carácter no coincide, indicar que no hay
coincidencia en esa posición (imprimiendo la posición) y continuar. Si se
encuentra una coincidencia, indicar en qué posición se encontró y
finalizar la ejecución.
"""


print("Ingresa una frase")
frase = str(input())
print("Ingrese una letra")
letra = str(input())

i=0
while i!=len(frase):
    if letra != frase[i]:
        print("No se encontró en la posición", i)
        i+=1
        continue
    print("Se encontró en la posición", i)
    break

"""
14.Crear un programa que permita al usuario ingresar los montos de las
compras de un cliente (se desconoce la cantidad de datos que cargará, la
cual puede cambiar en cada ejecución), cortando el ingreso de datos
cuando el usuario ingrese el monto 0.
Si ingresa un monto negativo, no se debe procesar y se debe pedir que

ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo
que cuenta que, si las ventas superan el total de $1000, se le debe
aplicar un 10% de descuento.
"""

print("Ingrese el monto de compra")
monto = int(input())
sum = 0

while True:
    if monto > 0:
        sum = sum + monto
        print("Ingrese el monto de compra")
        monto = int(input())
    if monto < 0:
        print("No se pueden procesar montos negativos, ingrese un nuevo monto ")
        monto = int(input())
    if monto == 0:
        break

if sum >= 1000:
    descuento = sum - (sum* 0.1)
    print("El total a pagar es ", descuento)
if sum < 1000:
    print("El total a pagar es ", sum)

"""
15.Crear un programa que solicite el ingreso de números enteros positivos,
hasta que el usuario ingrese el 0. Por cada número, informar cuántos
dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares
leídos en total.
"""

print("Ingrese un numero entero positivo")
num = int(input())
par = 0
impar = 0

while True:
    if num == 0:
        break
    if num % 2 == 0:
        par = par + 1
        print("Ingrese un numero entero positivo")
        num = int(input())
    if num % 2 == 1:
        impar = impar + 1
        print("Ingrese un numero entero positivo")
        num = int(input())

print("La cantidad de pares es ", par, "La cantidad de impares es ", impar)


"""
16.Escribir un programa que solicite el ingreso de una cantidad
indeterminada de números mayores que 1, finalizando cuando se reciba
un cero. Imprimir la cantidad de números primos ingresados.
"""

print("Ingrese un numero mayor a 1")
num = int(input())
cont = 0

while num != 0:
   primo = True
   for i in range(2, num):
      if num % i == 0:
        primo = False
        break
   if primo :
    cont = cont + 1
   print("Ingrese un numero")
   num = int(input())
        
print("La cantidad de primos es ", cont)

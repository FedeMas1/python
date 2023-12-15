"""
1. Un hombre desea saber cuánto dinero se genera por concepto de
intereses sobre la cantidad que tiene en inversión en el banco. El
decidirá reinvertir los intereses siempre y cuando estos excedan a
$7000, y en ese caso desea saber cuánto dinero tendrá finalmente en
su cuenta.

print("Deposito inicial")
DI= int(input())
print("Interes anual")
IA= int(input())
print("Plazo del deposito")
dias= int(input())

interes= DI*IA*dias/(100*365)
if interes>7000: 
    DF= round(DI + interes, 2) 
    print("El dinero final es ", DF)
else: 
    print("El interes es de ", interes)

    
2. Un obrero necesita calcular su salario semanal, el cual se obtiene de la
siguiente manera:
a. Si trabaja 40 horas o menos se le paga $3000 por hora
b. Si trabaja más de 40 horas se le paga $3000 por cada una de las
primeras 40 horas y un 50% más por cada hora extra.

print("Cuanta cantidad de horas a la semana trabaja?")
horas = int(input())

if horas > 40:
    salario = 40*3000 + (horas-40) * 150
else :
    salario = horas * 3000

print("El salario es ", salario)

3. Ingresar dos números distintos e imprimirlos en forma ascendente.

print("Ingrese un numero")
n1 = int(input())
print("Ingrese otro numero")
n2 = int(input())

if n1<n2:
    print(n1, ",", n2)
else:
    print(n2, ",", n1)

4. Una persona enferma, que pesa 65 kg, se encuentra en reposo y desea
saber cuántas calorías consume su cuerpo durante el tiempo ingresado
que realice una misma actividad. Las actividades que tiene permitido
realizar son únicamente dormir o estar sentado en reposo. Los datos
que tiene son que estando dormido consume 1.08 calorías por minuto y
estando sentado en reposo consume 1.66 calorías por minuto.

print("Cuantas horas durmió?")
durmiendo= int(input())
print("Cuantas horas estuvo en reposo?")
reposo = int(input())

CD = durmiendo*1.08
CR = reposo*1.66

print("La cantidad de calorias que gastó durmiendo es de:", CD ," La cantidad de calorias que gastó en reposo es de ",CR )

5. Hacer un algoritmo que imprima el nombre de un artículo, clave,
precio original y su precio con descuento. El descuento lo hace en base
a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el
descuento en del 20% (solo existen dos claves).



print("Nombre del articulo")
articulo = str(input())
print("Ingrese la clave")
clave = int(input())
print("Precio")
precio= int(input())

if clave == 1:
    descuento = precio - precio*0.1
else:
    descuento = precio - precio*0.2

print("El valor del producto con el descuento es de ", descuento)

6. Hacer un algoritmo que calcule el total a pagar por la compra de
camisas. Si se compran tres camisas o más se aplica un descuento del
20% sobre el total de la compra y si son menos de tres camisas un
descuento del 10%

"""
print("Precio de las camisas sin descuento")
precio = int(input())
print("Cuantas camisas llevó?")
cantidad = int(input())

if cantidad >= 3:
    descuento = precio - precio*0.2
if cantidad < 3:
    descuento = precio - precio *0.1

print("El precio con descuento es de ", descuento)
































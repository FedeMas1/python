"""
1. Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

print("Año en curso")
año = int(input())

for i in range(0, 3):
    print("Nombre")
    nombre = str(input())
    print("Año de nacimiento")
    nac= int(input())

    añoA= año - nac
    print(nombre, " cumplirá,", añoA, " este año")

"""
2. Pedir al usuario ingresar 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
"""

cont= 0
for i in range (0, 10):
    print("Ingrese su edad")
    edad= int(input())
    if edad > 20:
        cont = cont + 1
print(cont)

"""
3. Ingresar una serie de nombres. Al finalizar imprimir la cantidad de
comienzan con la letra que elija el usuario.
"""

print("Ingrese un nombre o Ñ para finalizar")
nombre = str(input())
print("Ingrese una letra")
letra = str(input())
cont = 0

while nombre != "ñ":
    if nombre == "ñ":
        break
    if nombre[0].lower() == letra:
        cont = cont + 1
        print("Ingrese un nombre o ñ para finalizar")
        nombre = str(input())
    else: 
        print("Ingrese un nombre o ñ para finalizar")
        nombre = str(input())
print(cont)

"""
4. Crear una función contar_vocales(), que reciba una palabra y cuente
cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas
las vocales.
"""

print("Escriba una palabra")
cadena = str(input())
i = 0
contA = 0
contE = 0
contI = 0
contO = 0
contU = 0


def contar_vocales (palabra):
    global contA, contE, contI, contO, contU
    for i in range (len(palabra)):
        if palabra[i].lower() == "a":
            contA = contA + 1
        if palabra[i].lower() == "e":
            contE = contE + 1
        if palabra[i].lower() == "i":
            contI = contI + 1
        if palabra[i].lower() == "o":
            contO = contO + 1
        if palabra[i].lower() == "u":
            contU = contU + 1

contar_vocales(cadena)
print("A =", contA, " E = ", contE, "I =", contI, "O =", contO, "U =", contU)

"""
5. Escribir un programa que almacene la cadena de caracteres de una
contraseña en una variable, pregunte al usuario por la contraseña e
imprima por pantalla si la contraseña introducida por el usuario coincide
con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

print("Ingrese la contraseña")
contra = str(input())
almacenado = []


for i in range (len(contra)):
    almacenado.append(contra[i].lower())

print("Introduzca la contraseña")
contraseña = str(input())

for i in range(len(contraseña)):
    if contraseña[i].lower() != almacenado[i]:
        print("Contraseña incorrecta")
        break

"""
6. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al
sexo y el nombre. El grupo A esta formado por las mujeres con un nombre
anterior a la M y los hombres con un nombre posterior a la N y el grupo B
por el resto. Escribir un programa que pregunte al usuario su nombre y
sexo, y muestre por pantalla el grupo que le corresponde.
"""  


print("Ingrese el nombre")
nombre = str(input())
print("Ingrese M por masculino y F por femenino")
sexo = str(input())

if sexo == "F" and ord(nombre[0]) < ord("M"):
    print("Pertenece al grupo A")
if sexo == "F" and ord(nombre[0]) >= ord("M"):
    print("Pertenece al grupo B")
if sexo == "M" and ord(nombre[0]) > ord("N"):
    print("Pertenece al grupo A")
if sexo == "M" and ord(nombre[0]) <= ord("N"):
    print("Pertenece al grupo B")

"""
7. Escribir un programa para una empresa que tiene salas de juegos para
todas las edades y quiere calcular de forma automática el precio que debe
cobrar a sus clientes por entrar. El programa debe preguntar al usuario la
edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de
4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si
es mayor de 18 años, $1000
"""

print("Ingrese la edad")
edad = int(input())

if edad < 4:
    print("La entrada es gratis")
if edad > 4 and edad < 18:
    print("La entrada cuesta $500")
if edad > 18:
    print("La entrada cuesta $1000")

    
"""
8. La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus
clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Espinaca y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y huevo.
Escribir un programa que pregunte al usuario si quiere una pizza
vegetariana o no, y en función de su respuesta le muestre un menú con los
ingredientes disponibles para que elija. Solo se puede elegir un ingrediente
además de la mozzarella y el tomate que están en todas la pizzas. Al final se
debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
ingredientes que lleva
"""

pizza=input("Quiere una pizza vegetariana? ")

if pizza == "si" :
    ingrediente=input("Elija su ingrediente entre Espiaca y tofu ")
    print("La pizza tiene Mozzarella, tomate y ", ingrediente)
elif pizza == "no":
    ingrediente= input("Elija un ingrediente entre pepperoni, jamon y huevo ")
    print("La pizza tiene mozzarella, tomate y ", ingrediente)

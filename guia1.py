"""
1. Escribí un programa que solicite al usuario dos números y los almacene
en dos variables. En otra variable, almacená el resultado de la suma de
esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un
tercer número, el cual se debe almacenar en una nueva variable. Por
último, mostrá en pantalla el resultado de la multiplicación de este nuevo
número por el resultado de la suma anterior.
"""

print("Ingrese un numero")
n1 = int(input())
print("ingrese otro numero")
n2 = int(input())
n3 = int(n1 + n2)
print("La suma de los numeros es", n3)

print("ingrese un numero distinto")
n4 = int(input())
print("El resultado de la multiplicacion es ", n3*n4)


"""
2. Escribí un programa que solicite al usuario ingresar la cantidad de
kilómetros recorridos por una motocicleta y la cantidad de litros de
combustible que consumió durante ese recorrido. Mostrar el consumo de
combustible por kilómetro.
"""

print("Ingrese la cantidad de kilometros recorridos")
km= int(input())
print("Ingrese la cantidad de litros de combustible gastados")
lt= int(input())
lxk= round(lt/km, 2)
print("El consumo por kilometro es de ", lxk)

"""
3. Escribí un programa que solicite al usuario un número y le reste el 15%,
almacenando todo en una única variable. A continuación, mostrar el
resultado final en pantalla.
"""

print("Ingrese un numero")
n= int(input())
rstd = float(n-n*0.15)
print("El resultado final es ", rstd)

"""
4. Escribí un programa que solicite al usuario el ingreso de dos palabras,
las cuales se guardarán en dos variables distintas. A continuación,
almacená en una variable la concatenación de la primera palabra, más
un espacio, más la segunda palabra. Mostrá este resultado en pantalla.
"""

print("Ingrese una palabra")
p1= str(input())
print("Ingrese otra palabra")
p2= str(input())
con = p1+" "+p2
print(con)

"""
5. Escribí un programa que le solicite al usuario su edad y la guarde en una
variable. Que luego solicite la cantidad de artículos comprados en una
tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un
valor de verdad (True o False) que indique si el usuario es mayor de 18
años de edad y además compró más de 1 artículo.
"""

print("Ingrese su edad")
edad= int(input())
print("Ingrese la cantidad de articulos comprados")
art= int(input())

if edad>=18 and art>=1 : print(True)
else: print(False)


#Ivan Diego Saenz Cotrina

print("\nPregunta 1.")
print("Realizar un programa que ingrese sus datos personales e imprimirlos.")
apellidos = input('Ingresa tus apellidos: ')
nombres = input('Ingresa tus nombres: ')
dni = int(input('Ingresa tu DNI: '))
numCelular = int(input('Ingresa tu # de telefono: '))
print("-----> Tu nombre completo es: "+apellidos+", "+nombres)
print(f"-----> Tu dni es {dni} y tu numero de celular es {numCelular}")



print("\nPregunta 2.")
print("Calcule el área de un círculo, triángulo y cuadrado con radio ingresado desde el teclado.")
import math
radioCirculo = float(input('Ingrese el radio para calcular el area del circulo: '))
print(f"-----> El area del circulo es: {math.pi*radioCirculo**2}")
baseTriangulo = float(input('\nIngrese la base para calcular el area del triangulo: '))
alturaTriangulo = float(input('Ingrese la altura para calcular el area del triangulo: '))
print(f"-----> El area del triangulo es: {(baseTriangulo*alturaTriangulo)/2}")
ladoCuadrado = float(input('\nIngrese el lado para calcular el area del cuadrado: '))
print(f"-----> El area del cuadrado es: {ladoCuadrado**2}")



print("\nPregunta 3.")
print("Ingrese 3 valores y realice las operaciones de suma, resta, multiplicación, división y división entera.")
valor1 = float(input('Ingrese el valor 1: '))
valor2 = float(input('Ingrese el valor 2: '))
valor3 = float(input('Ingrese el valor 3: '))
print(f"\n-----> La suma es: {valor1+valor2+valor3}")
print(f"-----> La resta es: {valor1-valor2-valor3}")
print(f"-----> La multiplicaciones es: {valor1*valor2*valor3}")
print(f"-----> La división es: {(valor1/valor2)/valor3}")
print(f"-----> La división entera es: {(valor1//valor2)//valor3}")



print("\nPregunta 4.")
print("Ingrese un valor e imprima el tipo de dato")
tipoDeDato = input("Ingrese un valor: ")
print(f"-----> El tipo de dato es: {type(tipoDeDato)}")



print("\nPregunta 5.")
print("Realice un programa que imprima la ubicación de su carpeta donde se encuentra trabajando.")
import sys
variable = sys.argv[0]
print(f"-----> La ubicacion es: {variable}")



print("\nPregunta 6.")
print("Realice un programa que calcule la suma de los números hasta el valor ingresado. \nEjemplo : si se ingresa 5 se tendrá que calcular 1+2+3+4+5.")
limiteSuperior = int(input('Ingrese el limite de la suma: '))
sumaTotal=0
i = 1
cadenaSuma = ""
while (i<=limiteSuperior):
    cadenaSuma = cadenaSuma +"+"+ str(i)
    sumaTotal=sumaTotal+i
    i = i+1
print(f"-----> El resultado de la suma de {cadenaSuma} es: {sumaTotal}")



print("\nPregunta 7.")
print("Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos: ")
print("● Si los dos números son iguales")
print("● Si los dos números son diferentes")
print("● Si el primero es mayor que el segundo")
print("● Si el segundo es mayor o igual que el primero")
primerNumero = float(input("Ingrese el valor del primer numero: "))
segundoNumero = float(input("Ingrese el valor del segundo numero: "))
if primerNumero==segundoNumero:
    print("-----> Los numeros son iguales")
else:
    print("-----> Los numeros son diferentes")
    if primerNumero>segundoNumero:
        print(f"-----> El primer numero ({primerNumero}) es mayor que el segundo numero ({segundoNumero})")
    else:
        print(f"-----> El segundo numero ({segundoNumero}) es mayor que el primero numero ({primerNumero})")



print("\nPregunta 8.")
print(
'''
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas
'''
)
passwordDelSistema = "contraseña"
passwordIngresada = input("Ingrese su contraseña: ")
if passwordIngresada.lower()==passwordDelSistema:
    print("-----> Las contraseñas coinciden")
else:
    print("-----> Contraseña incorrecta.")
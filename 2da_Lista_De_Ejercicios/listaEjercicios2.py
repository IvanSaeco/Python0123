from os import system, name # Para limpiar la terminal.

#Procedimiento para limpiar la terminal
def clear():
    if name == 'nt': # En caso de Windows
        _ = system('cls')
    else: # Para Mac o Linux
        _ = system('clear')

#Pregunta 1
clear()
print("\nEjercicio 1.")
print("Realizar un Menú Iterativo con las siguientes opciones")

while True:
    print("""\nMenú Iterativo del EJERCICIO 1
    1) Imprimir un cuadrado
    2) Identificar si es múltiplo de 2
    3) Imprimir mayores de edad de la lista
    4) Salir""")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        lado = int(input("Ingresa el lado del cuadrado: "))
        for i in range(lado):
            for i in range(lado):
                print('*',end = '  ')
            print()
        input("\nPresiona cualquier tecla para continuar...")
        clear()
    elif opcion == '2':
        lista = [21,48,99,46,12,111,1237,9874,223,222]
        print(f"La lista es: {lista}\n")
        for x in lista:
            if x%2==0:
                print(f"El numero {x} es multiplo de 2")
        input("\nPresiona cualquier tecla para continuar...")
        clear()
    elif opcion =='3':
        listaDePersonas = [["Juan", 18],["Miguel", 17],["Pedro", 22],["Rosa", 20],["Guadalupe", 16],["Maria", 32]]
        print(f"La lista es: {listaDePersonas}\n")
        for i in range(len(listaDePersonas)):
            if listaDePersonas[i][1]>=18:
                print(f"{listaDePersonas[i][0]} es mayor de edad, pues tiene {listaDePersonas[i][1]} años")
        input("\nPresiona cualquier tecla para continuar...")
        clear()
    elif opcion =='4':
        print("Saliendo del Menú Iterativo, gracias por su preferencia.")
        input("\nPresiona cualquier tecla para continuar...")
        clear()
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
        input("\nPresiona cualquier tecla para continuar...")
        clear()

#Pregunta 2
clear()
print("\nEjercicio 2.")
print("Realizar un Programa que simule funcionalidades de una Biblioteca, definir biblioteca como un diccionario")

bibliotecaLimaNorte = {
    "Usuarios" : ["Mariano","Pepe","Juan","Maria"],
    "Libros" : [["El viejo y el mar","Ernest Hemingway","Alegoria",False],
                 ["La Divina Comedia","Dante Alighieri","Epopeya",False],
                  ["Los 3 cerditos","Joseph Jacobs","Fabula",True],
                   ["Crimen y castigo","Fiodor Dostoyevski","Policial",False]],
}

#Funciones utilizadas
def nombreExiste(nombreLibro):
    for i in range(len(bibliotecaLimaNorte["Libros"])):
        if(bibliotecaLimaNorte["Libros"][i][0].lower()==nombreLibro.lower()):
            return True
    return False

def esPrestado(nombreLibro):
    for i in range(len(bibliotecaLimaNorte["Libros"])):
        if(bibliotecaLimaNorte["Libros"][i][0].lower()==nombreLibro.lower()):
            if(bibliotecaLimaNorte["Libros"][i][3]==False):
                return False
    return True

while True:
    print("""\nBiblioteca LIMA NORTE del EJERCICIO 2
    1) Listar las categorias de los libros disponibles
    2) Listar libros y su autor
    3) Cambiar el estado de un libro a prestado
    4) Listar usuarios de la biblioteca
    5) Salir""")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("\nCategorias disponibles:")
        for i in range(len(bibliotecaLimaNorte["Libros"])):
            print("* "+bibliotecaLimaNorte["Libros"][i][2])
        input("\nPresiona cualquier tecla para continuar...")
        clear()
    elif opcion =='2':
        print("\nLibros y su autor:")
        for i in range(len(bibliotecaLimaNorte["Libros"])):
            print("* "+bibliotecaLimaNorte["Libros"][i][0]+" - "+bibliotecaLimaNorte["Libros"][i][1])
        input("\nPresiona cualquier tecla para continuar...")
        clear()
    elif opcion =='3':
        for i in range(len(bibliotecaLimaNorte["Libros"])):
            print("* "+bibliotecaLimaNorte["Libros"][i][0])
        nombreLibro = input("Ingrese el nombre del libro cuyo estado desea cambiar a prestado (puede escribirlo con o sin mayusculas): ")
        if nombreExiste(nombreLibro)==True:
            if esPrestado(nombreLibro)==False:
                for i in range(len(bibliotecaLimaNorte["Libros"])):
                    if(bibliotecaLimaNorte["Libros"][i][0].lower()==nombreLibro.lower()):
                        bibliotecaLimaNorte["Libros"][i][3]=True
                        print("\nEl estado del libro se actualizo correctamente.")
                        input("\nPresiona cualquier tecla para continuar...")
                        clear()
            else:
                print("\nEste libro ya ha sido prestado.")
                input("\nPresiona cualquier tecla para continuar...")
                clear()
        else:
            print("\nEste libro no existe.")
            input("\nPresiona cualquier tecla para continuar...")
            clear()
    elif opcion =='4':
        print("\nUsuarios de la biblioteca:")
        for i in range(len(bibliotecaLimaNorte["Usuarios"])):
            print("* "+bibliotecaLimaNorte["Usuarios"][i])
        input("\nPresiona cualquier tecla para continuar...")
        clear()
    elif opcion =='5':
        print("Saliendo del Sistema Biblioteca LIMA NORTE, gracias por su preferencia.")
        input("\nPresiona cualquier tecla para continuar...")
        clear()
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
        input("\nPresiona cualquier tecla para continuar...")
        clear()


#Pregunta 3
clear()
print("\nEjercicio 3.")
print("Definir una funcion que retorne el mayor valor al ingresar 2 numeros")

def retornarMayorValor(numero1, numero2):
    if numero1 > numero2 :
        return numero1
    else:
        return numero2

numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
print(f"\nEl mayor numero es: {retornarMayorValor(numero1,numero2)}")
input("\nPresiona cualquier tecla para continuar...")

#Pregunta 4
clear()
print("\nEjercicio 4.")
print("Definir una funcion que imprima los argumentos ingresados")

import sys

def imprimirArgumentos(*args):
    return args
print('''
\x1B[3mFuncion:\x1B[0m
def imprimirArgumentos(*args):
    return args

\x1B[3mPrint realizado:\x1B[0m
print(imprimirArgumentos(1,True,"Ivan Diego"))
''')

print("\x1B[3mResultado:\x1B[0m ", end = "")
print(imprimirArgumentos(1,True,"Ivan Diego"))
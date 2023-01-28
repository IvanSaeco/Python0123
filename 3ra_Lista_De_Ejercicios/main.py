# Para limpiar la terminal.
from lib.clear import * 

#Importando los demas archivos respectivamente para cada pregunta. 
from lib.pregunta2 import *
from lib.pregunta3 import *
from lib.pregunta4 import Catalogo, Producto as Producto_P4 #Debido a que en la pregunta 7 tambien hay una clase Producto
from lib.pregunta5.sumaRecursivaPrimerosN import *
from lib.pregunta5.dividirDosNumeros import *
from lib.pregunta6 import *
from lib.pregunta7 import *
from lib.pregunta8 import *

#Condicion del main.py
if __name__=='__main__':
    while True:
        clear()
        print("""\nMenú Iterativo del main.py
        2) Ejercicio 2 - Funciones String al Texto
        3) Ejercicio 3 - Multiplicar por 2 y otra funcion
        4) Ejercicio 4 - Tienda de Auto Partes
        5) Ejercicio 5 - Suma Recursiva y Division de 2 Numeros
        6) Ejercicio 6 - Imprimir Nombre del Archivo en Ejecucion
        7) Ejercicio 7 - Procuto con nombre y codigo
        8) Ejercicio 8 - Pregunta 5 con Try y Except
        9) Salir""")
        opcion = input("Seleccione una opción: ")

        if opcion == '2':
            funcionesString()
            input("\nPresiona cualquier tecla para continuar...")
            clear()
        elif opcion == '3':
            enteroPorValor = int(input("Ingrese un numero a multiplicar por 2 y otra funcion: "))
            print(multiplicarPor2YOtraFuncion(enteroPorValor))
            input("\nPresiona cualquier tecla para continuar...")
            clear()
        elif opcion =='4':
            print("\nCreando objetos Producto y Agregandolos al objeto Catalogo por constructor y agregar()")
            catalogo = Catalogo([Producto_P4("Asiento Delantero",499,"Primax")])
            catalogo.agregar(Producto_P4("Motor",1999,"Duraccel"))
            print("\nUtilizando el metodo para mostrar toda la lista de productos")
            catalogo.mostrar()
            input("\nPresiona cualquier tecla para continuar...")
            clear()
        elif opcion =='5':
            print(f'La suma es: {sumaRecursivaPrimerosN(int(input("Ingrese el valor de N para la suma recursiva: ")))}')
            print("La division es: "+str(dividirDosNumeros(a=float(input("\nIngresa el 1er numero: ")),b=float(input("Ingresa el 2do numero: ")))))
            input("\nPresiona cualquier tecla para continuar...")
            clear()
        elif opcion =='6':
            imprimirNombreDelArchivoEnEjecucion()
            input("\nPresiona cualquier tecla para continuar...")
            clear()
        elif opcion =='7':
            productoP7 = Producto("Television4K", "PERU-0001-2023")
            print(productoP7)
            input("\nPresiona cualquier tecla para continuar...")
            clear()
        elif opcion =='8':
            pregunta5ConTryYExect()
            input("\nPresiona cualquier tecla para continuar...")
            clear()
        elif opcion =='9':
            print("Saliendo del Menú Iterativo, gracias por su preferencia.")
            input("\nPresiona cualquier tecla para continuar...")
            clear()
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
            input("\nPresiona cualquier tecla para continuar...")
            clear()

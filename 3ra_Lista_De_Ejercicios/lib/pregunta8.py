import os

def pregunta5ConTryYExect():
    try:
        from lib.pregunta5.sumaRecursivaPrimerosN import sumaRecursivaPrimerosN
        from lib.pregunta5.dividirDosNumeros import dividirDosNumeros
        print(f'La suma es: {sumaRecursivaPrimerosN(int(input("Ingrese el valor de N para la suma recursiva: ")))}')
        print("La division es: "+str(dividirDosNumeros(a=float(input("\nIngresa el 1er numero: ")),b=float(input("Ingresa el 2do numero: ")))))
    except:
        print("EXCEPTION: Ha ocurrido un error en el TRY")
    else:
        print("Todo ha funcionado correctamente, se procedera a imprimir la ruta.")
        print(f"Ruta: {os.getcwd()}")
    finally:
        print("FINALLY: Proceso terminado")
from os import system, name # Para limpiar la terminal.
#Procedimiento para limpiar la terminal
def clear():
    if name == 'nt': # En caso de Windows
        _ = system('cls')
    else: # Para Mac o Linux
        _ = system('clear')
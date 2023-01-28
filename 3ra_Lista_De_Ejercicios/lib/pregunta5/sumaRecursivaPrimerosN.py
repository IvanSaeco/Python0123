def sumaRecursivaPrimerosN(n):
    if n == 1:
        return 1
    else:
        return n + sumaRecursivaPrimerosN(n-1)
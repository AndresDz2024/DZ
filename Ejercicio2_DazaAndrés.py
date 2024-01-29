## -------------------------------------------------
## ------------------ Ejercicio2 -------------------
## -------------------------------------------------
## ------------------- arreglos --------------------

A = 0
B = 1

print("       Bienvenido usuario, te voy a explicar como funciona la serie de fibonacci: ")
print("-----------------------------------------------------------------------------------")
print("""       Se trata de una secuencia infinita de números naturales;
       a partir del 0 y el 1, se van sumando a pares, de manera que
       cada número es igual a la suma de sus dos anteriores""")
print("-----------------------------------------------------------------------------------")
N = input("ingresa hasta que numero de la secuencia fibonacci deseas ver: ")
def fibo(N):
    if (N < 2):
        return "N"
    else:
        return fibo(N-1) + fibo(N-2)

print(fibo(N))


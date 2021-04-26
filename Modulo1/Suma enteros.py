n = int(input("Introduce un número entero: "))
suma = n*(n+1)/2
 
if (type(n)==int):
    print("La suma de los números enteros desde 1 hasta " + str(n) + " es " + str(suma))

elif (type(n) == float):
    print("No es un entero.")

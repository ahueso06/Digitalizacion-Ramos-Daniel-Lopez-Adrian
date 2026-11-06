numero1 = int(input("introduce un numero entero"))
numero2 = int(input("introduce un numero entero menor que el numero 1"))
while numero1 < numero2:
    print ("El numero entero es mayor que el primero")
    numero2 = int(input("introduce un numero entero menor que el numero 1"))
suma = 0
for numero in range (numero1, numero2 -1, -1):
   suma += numero

print (f"La suma del {numero1} y el {numero2} es {suma}")
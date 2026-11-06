suma = 0
contador = 0
mayor = None
menor = None

numero = int(input("INTRODUCE UN NUMERO POSITIVO (INTRODUCE 0 PARA TERMINAR)"))

while numero > 0:
    suma += numero
    contador += 1
    if mayor is None and menor is None:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    numero = int(input("INTRODUCE UN NUMERO POSITIVO (INTRODUCE 0 PARA TERMINAR)"))
    media = suma / contador

print (f"se han introducido {contador} numeros, la suma total es {suma} y la media es {media} el mayor es {mayor} y el menor {menor}")
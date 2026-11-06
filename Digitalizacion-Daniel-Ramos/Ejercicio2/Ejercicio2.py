print("=== ADIVINA EL NÚMERO ===")

numero_secreto = 7

numero = int(input("Adivina el número del 1 al 10: "))

if numero == numero_secreto:
    print("¡Enhorabuena! Has acertado.")
else:
    print("No has acertado. El número era", numero_secreto)
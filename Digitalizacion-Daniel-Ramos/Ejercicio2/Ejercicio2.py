print("=== ADIVINA EL NÚMERO ===")

numero_secreto = 7

numero = int(input("Adivina el número del 1 al 10: "))
while numero != numero_secreto:
    print("No has acertado.")
    numero = int(input("Adivina el número del 1 al 10: "))
print ("!ENHORABUENA! Has acertado.")
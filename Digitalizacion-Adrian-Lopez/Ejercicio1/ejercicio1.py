factura_total = 0
numero_articulos = 0
precio = float(input(f"Introduce el importe del articulo {numero_articulos + 1}:"))
while precio > 0:
    cantidad = float(input(f"Introduce la cantidad del articulo {numero_articulos + 1}:"))
    numero_articulos += 1
    factura_total += precio * cantidad
    precio = float(input(f"\nIntroduce el importe del articulo {numero_articulos + 1} (o 0 para salir): "))
    print (f"La factura total es {factura_total}")
    
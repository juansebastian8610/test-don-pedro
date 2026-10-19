from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

total = 0
for linea in lineas[2:]:
    print("-", linea)
    precio = linea.split("$")[1]
    precio = precio.replace(".", "")
    total = total + int(precio)

print("Total de productos:", len(lineas[2:]))
print("Valor del inventario: $" + str(total))
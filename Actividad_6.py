inventario = {}
cantidad = int(input("Ingrese la cantidad de productos que va a registrar: "))
for i in range(cantidad):
    print(f"Productio: {i + 1}")
    codigo = input("Código del producto: ")
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    talla = input("Talla del producto: ")
    precio = input("Precio del producto: ")
    if precio < 0:
        print("Precio no valido, tien que ser mayor a 0")
        continue
    cantidad = int(input("Ingrese la cantidad del producto en stock: "))

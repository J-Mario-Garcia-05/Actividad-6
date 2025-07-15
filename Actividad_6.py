inventario = {}
cantidad = int(input("Ingrese la cantidad de productos que va a registrar: "))
for i in range(cantidad):
    print(f"Productio: {i + 1}")
    codigo = input("Código del producto: ")
    if codigo in inventario:
        print("El codigo que ingreso ya se encuentra registrado en otro producto.")
        continue
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto (hombre/mujer): ")
    talla = input("Talla del producto: ")
    precio = int(input("Precio del producto: Q."))
    if precio < 0:
        print("Precio no valido, tien que ser mayor a 0")
        continue
    cantidad = int(input("Ingrese la cantidad del producto en stock: "))
    if cantidad < 0:
        print("No puede ingresar una cantidad menor a 0.")
    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "talla": talla,
    }
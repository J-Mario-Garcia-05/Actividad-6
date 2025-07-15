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
    stock = int(input("Ingrese la cantidad del producto en stock: "))
    if stock < 0:
        print("No puede ingresar una cantidad menor a 0.")
    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "talla": talla,
    }

print("Productos registrados:")
for codigo, producto in inventario.items():
    print(f"\nCódigo del producto: {codigo}")
    print(f"Nombre del producto: {producto['nombre']}\tCategoria: {producto['categoria']}\tTalla: {producto['talla']}")
    print(f"Precio del producto: {producto['precio']}\tCantidad en stock: {producto['stock']}")

buscar = input("Ingrese el códgio del producto que desea buscar: ")
if buscar in inventario:
    print(f"Nombre del producto: {inventario[buscar]['nombre']}\tCategoria: {inventario[buscar]['categoria']}")
    print(f"Talla: {inventario[buscar]['talla']}\tPrecio del producto: {producto['precio']}")
    print(f"Cantidad en stock: {producto['stock']}")

    valor_total = producto["precio"] * producto["stock"]
    print(f"Valor total del producto en inventario: {valor_total}")
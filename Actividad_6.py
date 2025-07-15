inventario = {}
i = 1
cantidad = int(input("Ingrese la cantidad de productos que va a registrar: "))
while i <= cantidad:
    print(f"\nProducto {i}:")
    codigo = input("Código del producto: ")
    if codigo in inventario:
        print("El codigo que ingreso ya se encuentra registrado en otro producto, repita nuevamente el registro.")
        continue
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto (hombre/mujer/niño): ")
    if categoria != "hombre" and categoria != "mujer" and categoria != "niño":
        print("Categoría no válida, repita nuevamente el registro.")
        continue
    try:
        talla = int(input("Talla del producto: "))
        if talla < 0:
            print("Talla ingresada no válida, repita nuevamente el registro.")
            continue
        precio = int(input("Precio del producto: Q."))
        if precio < 0:
            print("Precio no valido, tien que ser mayor a 0, repita nuevamente el registro.")
            continue
        stock = int(input("Ingrese la cantidad del producto en stock: "))
        if stock < 0:
            print("No puede ingresar una cantidad menor a 0, repita nuevamente el registro.")
            continue
    except Exception as e:
        print("Ha ocurrido un error en el registro, " + str(e))
        continue
    inventario[codigo] = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "talla": talla,
        "stock": stock
    }
    i += 1
input("Presione ENTER para continuar")

print("\nProductos registrados:")
for codigo, producto in inventario.items():
    print(f"\nCódigo del producto: {codigo}")
    print(f"Nombre del producto: {producto['nombre']}\tCategoria: {producto['categoria']}\tTalla: {producto['talla']}")
    print(f"Precio del producto: Q.{producto['precio']}\tCantidad en stock: {producto['stock']}")

buscar = input("\nIngrese el código del producto que desea buscar: ")
if buscar in inventario:
    print(f"Nombre del producto: {inventario[buscar]['nombre']}\tCategoria: {inventario[buscar]['categoria']}")
    print(f"Talla: {inventario[buscar]['talla']}\tPrecio del producto: Q.{inventario[buscar]['precio']}")
    print(f"Cantidad en stock: {inventario[buscar]['stock']}")
    valor_total = inventario[buscar]["precio"] * inventario[buscar]["stock"]
    print(f"Valor total del producto en inventario: Q.{valor_total:.2f}")
else:
    print("No existe el producto en inventario.")
input("Presione ENTER para continuar")

print("\nCantidad por categoría:")
cantidad_producto = 0
producto_mujer = 0
producto_hombre = 0
for codigo, producto in inventario.items():
    if producto['categoria'] == "mujer":
        producto_mujer += producto['stock']
    elif producto['categoria'] == "hombre":
        producto_hombre += producto['stock']
    else:
        cantidad_producto += producto['stock']
print(f"Productos de niño: {cantidad_producto}")
print(f"Productos de mujer: {producto_mujer}")
print(f"Productos de hombre: {producto_hombre}")
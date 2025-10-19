# GESTIÓN DE PRODUCTOS MEDIANTE LA MANIPULACIÓN DE ARCHIVOS

#1- Crear

lineas=[
    "coca-cola,3000,30\n",
    "sprite,2900,25\n",
    "fanta,2900,35\n"
]

with open("productos.txt", "w") as productos:
    for linea in lineas:
        productos.write(linea)

def cargar_productos():
    productos_diccionario = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            datos = linea_limpia.split(",")
            producto_registrado = {
                "nombre": datos[0],
                "precio": int(datos[1]),
                "cantidad": int(datos[2])
            }
            productos_diccionario.append(producto_registrado)
    return productos_diccionario

def guardar_productos(lista_productos):
    with open("productos.txt", "w") as archivo:
        for producto in lista_productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Productos guardados correctamente")

productos_diccionario = cargar_productos()
while True:
    print("## MENÚ DE GESTIÓN DE PRODUCTOS ##")
    print("1. Ver productos")
    print("2. Agregar producto")
    print("3. Buscar producto")
    print("4. Guardar y salir")
    
    opcion = input("Ingrese su opción: ")
    
    match opcion:
        case "1":
            print("\nProductos disponibles:")
            for producto in productos_diccionario:
                print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Stock: {producto['cantidad']}")
        
        case "2":
            nuevo_nombre = input("Ingrese el nombre del producto: ").lower()
            nuevo_precio = int(input("Ingrese el precio: "))
            nueva_cantidad = int(input("Ingrese la cantidad: "))

            nuevo_producto = {
                "nombre": nuevo_nombre,
                "precio": nuevo_precio,
                "cantidad": nueva_cantidad
            }
            productos_diccionario.append(nuevo_producto)
            print("Producto agregado")
        
        case "3":
            busqueda = input("Ingrese el nombre o parte del nombre: ").lower()
            encontrado = False
            
            for producto in productos_diccionario:
                if busqueda in producto['nombre']:
                    print(f"Encontrado: {producto['nombre']} - ${producto['precio']} - {producto['cantidad']} unidades")
                    encontrado = True
            if not encontrado:
                print("No se encontró el producto")
        
        case "4":
            guardar_productos(productos_diccionario)
            print("¡Hasta luego!")
            break
        
        case _:
            print("Opción inválida")

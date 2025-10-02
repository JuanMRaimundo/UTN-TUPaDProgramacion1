from math import inf
import random

#1) Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja

notas=[8,7,6,5,9,10,10,8,7,9]
suma=0
menor=+inf
mayor=-inf

for i in notas:
    suma=suma+i
promedio=suma/10  

for i in notas:
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i

print(f"Listado de notas: {notas}")
print(f"El promedio es: {promedio}")
print(f"La nota más alta es un {mayor}")
print(f"La nota más baja es un {menor}")


#2) Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista


productos=[]
seleccion=0
print("Hola! A continuación, podrás cargar 5 productos a tu lista: ")

for i in range(0,5):
    i+=1
    producto=input("Ingrese el producto: ")
    productos.append(producto)

productos.sort()

print("Estos son los productos ingresados:")
for i,producto in enumerate(productos):
    print(f"{i+1})-{producto}")

seleccion=int(input("Ingrese el número del producto que desea eliminar: "))
productos.pop(seleccion-1)
print("Esta es la lista actualizada: ")
for i,producto in enumerate(productos):
    print(f"{i+1})-{producto}")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#• Crear una lista con los pares y otra con los impares. 
#• Mostrar cuántos números tiene cada lista. 




numeros=[]
pares=[]
impares=[]
num_rand=0

for i in range (0,15):
    num_rand= random.randint(1,100)
    numeros.append(num_rand)

for num in numeros:
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)
cantidad_pares = enumerate(pares)
cantidad_impares = enumerate(impares)


print(f"Estos son los números pares: {pares}")
print(f"Estos son los números impares: {impares}")


#4) Dada una lista con valores repetidos: 
#• Crear una nueva lista sin elementos repetidos. 
#• Mostrar el resultado.

datos= [1,3,5,3,7,1,9,5,3]
nueva_lista=[]

for dato in datos:
    if dato not in nueva_lista:
        nueva_lista.append(dato)

print(f"Esta es la lista sin números repetidos: {nueva_lista}")

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#• Mostrar la lista final actualizada.


alumnos=["PEDRO SÁNCHEZ", "CLARA BERRA", "EMILIANO JANTULA", "FEDERICO PÁEZ", "ALFREDO MONTES", "GERMÁN ALCA", "MARÍA FERRO", "EZEQUIEL GONZÁLEZ"]

print("Estos son los estudiantes presentes en la clase: ")

for i,alumno in enumerate(alumnos):
    print(f"{i+1})- {alumno}")



while True:
        respuesta=input("Ingrese la opción de la operación que desea realizar:\n1-Agregar estudiante\n2-Eliminar estudiante\n3-Salir  ")

        match respuesta:
               
                case "1":
                        nombre=input("Ingrese el nombre del estudiante faltante: ").upper()
                        print(f"Usted ingresó el nombre de: {nombre}")
                        alumnos.append(nombre)

                case "2":
                        nombre=input("Ingrese el nombre del estudiante que desea eliminar: ").upper()
                        print(f"Usted eliminará el nombre de: {nombre}")
                        if nombre in alumnos:
                                alumnos.remove(nombre)
                                print(f"Se eliminó a {nombre}")
                        else:
                                print("Ese nombre no está en la lista")    

                case "3":
                        print("A continuación mostraremos la lista actualizada")            
                        break



print("Esta es la lista actualizada: ")
for i,alumno in enumerate(alumnos):
    print(f"{i+1})- {alumno}")


    
#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#último pasa a ser el primero). 
  
    
lista= [1,2,3,4,5,6,7]
ultimo = len(lista)-1
nueva_lista=[lista[ultimo]]
lista.pop()
nueva_lista=nueva_lista+lista
print(nueva_lista)

#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
#semana. 
#• Calcular el promedio de las mínimas y el de las máximas. 
#• Mostrar en qué día se registró la mayor amplitud térmica. 

minima=0
maxima=0
prom_min=0
prom_max=0
indice=0
diferencias=[]
mayor_amplitud=0
temperaturas_sem=[
    [10,17],
    [12,25],
    [11,26],
    [9,29],
    [13,30],
    [10,26],
    [8,22], 
]    

for i,temperatura in enumerate(temperaturas_sem):
    minima= temperatura[0]+minima
    maxima=temperatura[1]+maxima
    resta=temperatura[1]-temperatura[0]
    diferencias.append(resta)
mayor_amplitud= max(diferencias)  

        
print(f"El promedio de temperaturas minimas es de {minima/len(temperaturas_sem)} grados.")        
print(f"El promedio de temperaturas máximas es de {maxima/len(temperaturas_sem)} grados.")        
print(f"La mayor amplitud térmica fué de {max(diferencias)} grados, y se registró en el día {(diferencias.index(mayor_amplitud)+1)}")            


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#• Mostrar el promedio de cada estudiante. 
#• Mostrar el promedio de cada materia. 

promedio_est=0
promedio_mat=0
promedio=0
notas=[
    [7,8,6],
    [10,8,9],
    [5,8,7],
    [4,6,7],
    [9,8,8],
]
print("Estos son los Promedios de los estudiantes")

for i,estudiante in enumerate(notas):
    suma=0
    for nota in estudiante:
        suma+=nota
    print(f"Estudiante {i+1}: Promedio: {suma/3}")

       
print("Estos son los Promedios por Materia")

for num_materia in range(3):  
    suma=0
    for i,estudiante in enumerate(notas):
        suma+=estudiante[num_materia]
    print(f"Promedio: {suma/5}")

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#• Inicializarlo con guiones "-" representando casillas vacías. 
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#• Mostrar el tablero después de cada jugada. 
marca=""
turno=""
fila=0
columna=0
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("Este es el TA-TE-TI! Mostraremos el trablero para comenzar a jugar: ")
print(tablero)
for jugada in range(9):
        
        if (jugada%2)==0:
            turno = "O"
        else:
             turno = "X"

        while True:
            fila = int(input(f"Juega la {turno}: ingrese fila (0-2): "))
            columna = int(input(f"Juega la {turno}: ingrese columna (0-2): "))     
        
            
            if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                print("Error: fuera de rango")
                continue
            
            if tablero[fila][columna] != "-":
                print("Error: casilla ocupada")
                continue
            break
        tablero[fila][columna] = turno


        for fila_tablero in tablero:
            print(fila_tablero)
                
#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#• Mostrar el total vendido por cada producto. 
#• Mostrar el día con mayores ventas totales. 
#• Indicar cuál fue el producto más vendido en la semana. 

productos = [
    [10, 5, 6, 9],
    [14, 2, 6, 3],
    [2, 8, 4, 6],
    [14, 9, 5, 8],
    [6, 9, 2, 1],
    [0, 5, 4, 3],
    [7, 4, 1, 0],
]


print("Total vendido por producto:")
for num_producto in range(4): 
    total = 0
    for dia in productos:  
        total += dia[num_producto]
    print(f"Producto {num_producto + 1}: {total} unidades")

print()


print("Ventas totales por día:")
ventas_por_dia = []
for i, dia in enumerate(productos):
    total_dia = sum(dia)  
    ventas_por_dia.append(total_dia)
    print(f"Día {i + 1}: {total_dia} unidades")

dia_mayor_venta = ventas_por_dia.index(max(ventas_por_dia))
print(f"\nEl día con mayores ventas fue el día {dia_mayor_venta + 1} con {max(ventas_por_dia)} unidades")

print()

print("Producto más vendido:")
ventas_por_producto = []
for num_producto in range(4):
    total = 0
    for dia in productos:
        total += dia[num_producto]
    ventas_por_producto.append(total)

producto_mas_vendido = ventas_por_producto.index(max(ventas_por_producto))
print(f"El producto más vendido fue el Producto {producto_mas_vendido + 1} con {max(ventas_por_producto)} unidades")                
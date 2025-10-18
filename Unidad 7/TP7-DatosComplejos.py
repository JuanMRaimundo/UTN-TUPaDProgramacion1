#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print(precios_frutas)
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print(precios_frutas)
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print(precios_frutas)
precios_frutas["Naranja"]=1200
precios_frutas["Manzana"]=1500
precios_frutas["Pera"]=2300
print(precios_frutas)
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
print(precios_frutas)
lista_frutas=list(precios_frutas)
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.


contactos={}

for i in range(5):
    nombre=input("Ingrese el nombre: ").upper()
    telefono=int(input("Ingrese el número telefónico: "))
    contactos[nombre]=telefono

consulta_nombre=input("Ingrese el nombre que desea consultar: ").upper()

if consulta_nombre in contactos:
    print(f"El número de teléfono de {consulta_nombre} es: {contactos[consulta_nombre]}.")
else:
    print("Error: El nombre ingresado no se encuentra en la agenda telefónica.")

print(contactos)
print(consulta_nombre)    


#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.


frase=input("Ingrese la frase que desee: ")
palabras = frase.split()
set_frase= set(palabras)
contador_palabras=len(set_frase)
diccionario_palabras_rep={}

for palabra in set_frase:
    cantidad= palabras.count(palabra)
    diccionario_palabras_rep[palabra]=cantidad






print(f"Esta es la frase: {frase}")
print(f"Estas son las palabras ingresadas: {set_frase}")
print(f"Estas son las palabras repetidas: {diccionario_palabras_rep}")


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.


alumnos={}


for i in range(3):
    alumno_nombre=input("Ingrese el nombre del alumno: ")
    notas=()
    for al in range(3):
        nota=int(input("Ingrese las tres notas del alumno anteriormente mencionado: "))
        notas= notas + (nota,)
    alumnos[alumno_nombre]=notas

for nombre, notas in alumnos.items():
    promedio=sum(notas)/3
    print(f"{nombre}: {notas} - Promedio: {promedio}")


print(f"Estos son todos los alumnos con sus notas: {alumnos}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#y Parcial 2: 
#• Mostrá los que aprobaron ambos parciales. 
#• Mostrá los que aprobaron solo uno de los dos. 
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial1 = {1, 2, 3, 4, 5}      
parcial2 = {3, 4, 5, 6, 7}  

aprobaron_ambos=parcial1 & parcial2
aprobaron_almenos_uno= parcial1 | parcial2
aprobaron_uno=parcial1 ^ parcial2

print(f"Aprobaron ambos: {aprobaron_ambos}")
print(f"Aprobaron solo uno: {aprobaron_uno}")
print(f"Aprobaron al menos uno: {aprobaron_almenos_uno}")

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#Permití al usuario: 
#• Consultar el stock de un producto ingresado. 
#• Agregar unidades al stock si el producto ya existe. 
#• Agregar un nuevo producto si no existe.

productos= {
    "lavandina":23,
    "jabon_liquido":30,
    "limpiador_piso":52,
    "insecticida":42
}

while True:
    print("## Menú de gestión de stock: ##")
    print(productos.keys())
    opcion=input("A continuación, opciones de operaciones: \n1- Consulta de stock. \n2- Agregar stock a producto existente. \n3- Agregar nuevo producto a la lista. \n4- Salir del menú. ")
    match opcion:

        case "1":
            producto = input("Ingrese el nombre del producto a consultar: ").lower()
            if producto in productos:
                print(f"El stock de {producto} es: {productos[producto]} unidades")
            else:
                print("Ese producto no existe en el inventario")

        case "2":
            for i, (producto, stock) in enumerate(productos.items(), 1):
                     print(f"{i})- {producto}: {stock} unidades")
            lista_productos = list(productos.keys()) 
            numero_elegido = int(input("Ingrese el número: ")) - 1
            while numero_elegido >0 or numero_elegido >= len(lista_productos):     
                producto = lista_productos[numero_elegido] 
                cantidad = int(input("¿Cuántas unidades desea agregar? "))
                if cantidad < 0 :
                     print("Error: debe ingresar un numero positivo.")
                elif cantidad > 20:
                     print("Error: el sistema permite ingresar hasta 20 unidades por ineteno.")
                else:          
                    productos[producto] += cantidad   
                    print(f"Usted agregó {cantidad} unidades al producto {producto}.")
                break 
        case "3":
                nuevo_producto=input("A continuación ingrese el producto que desea agregar: ").lower()
                if nuevo_producto in productos:
                     print("Error: el producto ya existe en la lista. ")
                else: 
                    stock_inicial = int(input("Ingrese el stock inicial: "))
                    productos[nuevo_producto] = stock_inicial
                    print(f"Producto {nuevo_producto} agregado con {stock_inicial} unidades.")
                continue   
        case "4":
            print("## ADIOS! HASTA LA PRÓXIMA! ##")     
            break       
         
   #9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
#Permití consultar qué actividad hay en cierto día y hora.


agenda = {
    ("lunes", "9:00"): "Reunión de equipo",
    ("lunes", "11:00"): "Revisar proyectos",
    ("lunes", "14:00"): "Capacitación",
    ("martes", "9:30"): "Inicio Sprint",
    ("martes", "12:00"): "Almuerzo con cliente",
    ("martes", "15:00"): "Cierre de tareas",
    ("miércoles", "9:00"): "Planificación diaria",
    ("miércoles", "10:30"): "Desarrollo de features",
    ("miércoles", "13:00"): "Testing",
    ("jueves", "9:00"): "Daily standup",
    ("jueves", "11:00"): "Code review",
    ("jueves", "14:30"): "Documentación",
    ("viernes", "9:00"): "Retrospectiva",
    ("viernes", "11:00"): "Cierre de sprint",
    ("viernes", "15:00"): "Happy hour",
}
dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")
clave = (dia, hora)
if clave in agenda:
    print(f"El evento es: {agenda[clave]}")
else:
    print("No hay evento programado")

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#diccionario donde: 
#• Las capitales sean las claves. 
#• Los países sean los valores. 

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Perú": "Lima",
    "Bolivia": "La Paz",
    "Uruguay":"Montevideo",
    "Paraguay":"Asunción"
    }

capitales={}
for pais, capital in paises.items():
    capitales[capital] = pais
    
print("Estas son las capitales:")
for capital, pais in capitales.items():
    print(f"{capital} -> {pais}")
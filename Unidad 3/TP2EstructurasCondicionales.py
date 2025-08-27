import random
from statistics import mean, median, mode

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


edad_usuario = int(input("Ingrese su edad: "))

if  edad_usuario > 18: 
    print("Es mayor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.

nota= int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:   
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.


num = int(input("Ingrese un número par: "))


if ( num%2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")  


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.


edad_usuario = int(input("Ingrese su edad: "))

if edad_usuario >=0 and edad_usuario < 12:
    print("Es un Niño/a")
elif edad_usuario >= 12 and edad_usuario < 18:
    print("Es un Adolescente")    
elif edad_usuario >= 18 and edad_usuario < 30: 
    print("Es un Adulto/a joven") 
elif edad_usuario >=30 and edad_usuario<120:
    print("Es un Adulto") 
else:
    print("Ingrese una edad correcta")              


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contrasenia=input("Ingrese su nueva contraseña: ")
largo_contraseña= len(contrasenia)

if largo_contraseña>=8 and largo_contraseña <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")  

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. 
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla


num_aleatorios = [random.randint(1, 100) for i in range(50)]

media=mean(num_aleatorios)
mediana= median(num_aleatorios)
moda= mode(num_aleatorios)

if media > mediana and mediana > moda:
    print("El sesgo es positivo")
elif media<mediana and mediana < moda:
    print("El sesgo es negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Disculpe las molestias, hay un error en el servidor")    
    
    
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

frase=input("A continuación ingrese una frase o palabra: ")

ultima_letra=frase[-1] #En esta variable, estoy guardando la última letra de la palabra o frase ingresada para luego compararla

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(frase+"!")
else:
    print(frase)   


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.


nombre=input("A continuación ingrese su nombre: ")
print("A continuación, ingrese una opción (1,2 o 3), según las siguientes opciones: ")
opcion=int(input("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro..:  "))

if opcion==1:
    print(nombre.upper())  
elif opcion==2:
    print(nombre.lower())
elif opcion==3:
    print(nombre.title())
else:
    print("Por favor, ingrese una opcion correcta.")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 


magnitudIngresada=float(input("A continuación ingrese la magnitud del terremoto para indicar la categoría según la escala de Richter: "))

if magnitudIngresada < 3:
    print("Muy Leve (imperceptible)")
elif magnitudIngresada >= 3 and magnitudIngresada < 4:
    print("Leve (ligeramente perceptible)")  
elif magnitudIngresada >= 4 and magnitudIngresada < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")  
elif magnitudIngresada >= 5 and magnitudIngresada < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")  
elif magnitudIngresada >= 6 and magnitudIngresada < 7:
    print("Muy Fuerte (puede causar daños significativos)")  
elif magnitudIngresada >= 7:
    print("Extremo (puede causar graves daños a gran escala)")  
else:
    print("El valor ingresado es incorrecto.")    


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano. 

hemisferio=input("A continuación ingrese el hemisferio en el cual se encuentra:\n-N (si se encuentra en el hemisferio norte)\n-S (si se encuentra en el hemisferio sur): ")
mes=int(input("Ingrese el mes utilizando las siguientes opciones: \n1-Enero\n2-Febrero\n3-Marzo\n4-Abril\n5-Mayo\n6-Junio\n7-Julio"
"\n8-Agosto\n9-Septiembre\n10-Octubre\n11-Noviembre\n12-Diciembre --->"))

if mes <1 or mes > 12:
    print("El valor ingresado es incorrecto. Puede ser que el cálculo falle.")

dia=int(input("Ingrese el día de la fecha en número: "))

if dia <1 or dia > 31:
    print("El valor ingresado es incorrecto. Puede ser que el cálculo falle.")

if hemisferio=="N" or hemisferio=="n":

    if (mes==12 and dia >=21) or mes ==1 or mes==2 or (mes==3 and dia<=20):
        print("La estación del año es Invierno")
    elif  (mes==3 and dia >=21) or mes==4 or mes==5 or (mes==6 and dia <=20):
        print("La estación del año es Primavera")  
    elif  (mes==6 and dia >=21) or mes==7 or mes==8 or (mes==9 and dia <=20):
        print("La estación del año es Verano")   
    elif  (mes==9 and dia >=21) or mes==10 or mes==11 or (mes==12 and dia <=20):
        print("La estación del año es Otoño")  
    else: 
        pass

elif  hemisferio=="S" or hemisferio=="s":

    if (mes==12 and dia >=21) or mes ==1 or mes==2 or (mes==3 and dia<=20):
        print("La estación del año es Verano")
    elif  (mes==3 and dia >=21) or mes==4 or mes==5 or (mes==6 and dia <=20):
        print("La estación del año es Otoño")  
    elif  (mes==6 and dia >=21) or mes==7 or mes==8 or (mes==9 and dia <=20):
        print("La estación del año es Invierno")   
    elif  (mes==9 and dia >=21) or mes==10 or mes==11 or (mes==12 and dia <=20):
        print("La estación del año es Primavera")  
    else: 
        pass

else:
    print("La opción ingresada es incorrecta.")     

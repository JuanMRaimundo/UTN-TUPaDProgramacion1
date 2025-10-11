from math import pi
#1) Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Funciones

def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa Principal
imprimir_hola_mundo()

#2) Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.


# Funciones


def saludar_usuario(nombre):
    print(f"Hola {nombre}")
    

#Programa Principal

nombre=input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3) Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
#dir los datos al usuario y llamar a esta función con los valores in
#gresados.

# Funciones
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


#Programa Principal

nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su lugar de residencia: ")

informacion_personal(nombre,apellido,edad,residencia)



#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
#dio como parámetro y devuelva el área del círculo. calcular_peri
#metro_circulo(radio) que reciba el radio como parámetro y devuel
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am
#bas funciones para mostrar los resultados.


# Funciones

def calcular_area_circulo(radio):
    return pi*(radio**2)
def calcular_perimetro(radio):
    return 2*pi*radio

#Programa Principal

radio=int(input("Ingrese el radio del círculo: "))

print(f"El área del círculo es: {calcular_area_circulo(radio)}.")
print(f"El perímetro del circulo es2: {calcular_perimetro(radio)}")

#5) Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
#trar el resultado usando esta función.

# Funciones

def segundos_a_horas(segundos):
    return segundos/3600


#Programa Principal

segundos=int(input("Ingrese los segundos: "))
print(f"Para {segundos} seg ----> son: {segundos_a_horas(segundos)} horas!")

#6) Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
#ción.

# Funciones
def tabla_multiplicar(numero):
    print(f"## LA TABLA DEL {numero} DEL 0 AL 10!! ##")
    for i in range(0,11):
        multi=numero*i
        print(f"{numero} x {i} = {multi}")

#Programa Principal

numero=int(input("Ingrese un número: "))
tabla_multiplicar(numero)

#7) Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
#do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#sultados de forma clara.


# Funciones

def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=round(a/b,2)
    resultado= (suma,resta,multiplicacion,division)

    return resultado 

#Programa Principal

print("A continuación ingrese dos números para realizar las operaciones básicas: ")
a=int(input("Ingrese el primer número: "))
b=int(input("Ingrese el segundo número: "))

resultado=operaciones_basicas(a,b)

print(f"Los resultados son: \nSUMA={resultado[0]}\nRESTA={resultado[1]}\nMULTIPLICACIÓN={resultado[2]}\nDIVISIÓN={resultado[34]} ")


#8) Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
#ción para mostrar el resultado con dos decimales.

# Funciones

def calcular_imc(peso,altura):
    return round(peso/altura,2)


#Programa Principal

print("Para calcular su IMC, a continuación, ingrese su peso en KG y su altura en METROS.")
peso=int(input("Ingrese su peso en kilogramos: "))
altura=float(input("Ingrese su altura en metros: "))

print(f"Su IMC es de : {calcular_imc(peso,altura)}. ")

#9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.


# Funciones

def celcius_a_fahrenheit(celcius):
    return celcius + 32

#Programa Principal
celcius=float(input("Ingrese la temperatura en grados celcius: "))
print(f"La temperatura en Fahrenheit es de : {celcius_a_fahrenheit(celcius)}°F")

#10) Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Funciones

def calcular_promedio(a,b,c):
    return round((a+b+c)/3,2)


#Programa Principal
print("A continuación ingrese tres números para calcular su promedio: ")
a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segundo número: "))
c=float(input("Ingrese el tercer número: "))

print(f"El promedio es: {calcular_promedio(a,b,c)}")
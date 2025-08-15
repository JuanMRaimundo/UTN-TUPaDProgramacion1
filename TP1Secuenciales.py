# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

from math import pi


print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
##por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
##realizar la impresión por pantalla.

nombre=input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}! Bienvenido")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla

nombre=input("Por favor, ingrese su nombre: ")
apellido=input("Por favor, ingrese su apellido: ")
edad=input("Por favor, ingrese su edad: ")
residencia=input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio=int(input("Por favor, ingrese el radio de la circunferencia: "))
area=pi*radio**2
perimetro=2*pi*radio

print(f"El área de la circunferencia es:dfg {area} y el perímetro es: {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

seg=int(input("Ingrese la cantidad de segundos: "))
minutos= seg*60 
print(f"La cantidad de minutos es: {minutos}")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

num1=int(input("Ingrese un número para crear su tabla de multiplicar: "))
print(f"1 x {num1} = {num1*1}")
print(f"2 x {num1} = {num1*2}")
print(f"3 x {num1} = {num1*3}")
print(f"4 x {num1} = {num1*4}")
print(f"5 x {num1} = {num1*5}")
print(f"6 x {num1} = {num1*6}")
print(f"7 x {num1} = {num1*7}")
print(f"8 x {num1} = {num1*8}")
print(f"9 x {num1} = {num1*9}")
print(f"10 x {num1} = {num1*10}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese dos números enteros distintos de 0. Por favor, ingrese el primero: "))
num2 = int(input("Ingrese el segundo: "))
print(f"La suma de los dos números es: {num1+num2}")
print(f"La resta de los dos números es: {num1-num2}")
print(f"La división de los dos números es: {num1*num2}")
print(f"La multiplicación de los dos números es: {num1/num2}")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

print("Para calcular su Índice de masa corporal, deberá ingresar los siguientes datos: ")
altura=float(input("Ingrese su altura en metros: "))
peso=float(input("Ingrese su peso en kg: "))
imc=peso/(altura**2)
print(f"Su índice de masa corporal es de: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

tempCelcius=float(input("Ingrese la temperatura en Celcius para pasar a Fahrenheit: "))
tempFahren= (tempCelcius*(9/5))+32
print(f"La temperatura en Fahrenheit es de: {tempFahren}°F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números

num1=float(input("A continuación ingrese 3 números para calcular el promedio entre ellos. Ingrese el primero: "))
num2=float(input("Ingrese el segundo: "))
num3=float(input("Ingrese el tercero: "))
promedio= (num1+num2+num3)/3
print(f"El promedio es: {promedio}")

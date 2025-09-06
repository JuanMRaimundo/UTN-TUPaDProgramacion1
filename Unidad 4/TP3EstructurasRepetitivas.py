import random
from math import trunc

#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(1,101,1):
    print(x)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

num=int(input("A continuación ingrese un número: "))
cont=0
while num > 0:
    num=num // 10
    cont=cont +1
print(f"El número ingresado contiene {cont} dígitos.")    

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
sum=0
##El condicional es para que logren sumarse los numeros entre los extremos indicados por el usuario, sin importar cual ingresa primero.
if num1 > num2: 

    for cont in range(num2 +1, num1):
        sum= cont + sum 
        
    print(f"La sumatoria de los número comprendidos entre el {num1} y el {num2} es de: {sum}")

elif num1 < num2:
    for cont in range(num1 + 1,num2): 
       sum= cont + sum 
    print(f"La sumatoria de los número comprendidos entre el {num1} y el {num2} es de: {sum}")     

else:
    
    print(f"No hay números comprendidos entre {num1} y {num2} para sumar.")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
num=0
print("Ingrese números enteros para que puedan ser sumados. Para terminar la suma y mostrar el resultado, debe ingresar un cero.")
num=int(input("A continuación, ingrese el número: "))
sum=0

while num != 0:
    sum=sum + num
    num=int(input("Ingrese el otro número, o un cero para finalizar la suma: "))
  

print(f"La suma de los números ingresados es: {sum}. ")    


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.


num_aleatorio= random.randint(0,9)
num_usuario=int(input("Adivina el número sorteado entre el 0 y el 9 incluídos: "))

if num_usuario == num_aleatorio:
    print("Lo lograste, el número ganador es el: ", num_usuario)
else:    
    while num_usuario != num_aleatorio:
       num_usuario=int(input("Estuviste cerca! Vamos con otro inento: ")) 
print("Lo lograste! El número sorteado es el:", num_aleatorio)

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for x in range(100,-1,-2):
    print(x)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

num = int(input("Ingrese un número: "))
sum=0
for cont in range(0,num +1):
    sum= cont + sum
print("La suma de los valores comprendidos entre el 0 y el número ingresao es de: ", sum)   


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).   

pares=0
impares=0
positivos=0
negativos=0

for x in range(0,100,1):
    num=int(input("Ingrese el número: "))
    if num%2==0:
        pares+=1
    else:
        impares+=1
    if num >=0:
        positivos+=1
    else:
        negativos+=1            

print(f"Los números pares fueron: {pares}")
print(f"Los números impares fueron: {impares}")
print(f"Los números positivos fueron: {positivos}")
print(f"Los números negativos fueron: {negativos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
sum=0
cont=100
for x in range(cont):
    num=int(input("Ingrese un número: "))
    sum+=num
print(f"La media de los números ingresados es: {sum/cont}")    

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


num=0
digito=0
numInver=0

num=int(input("Ingrese un número: "))

while num !=0:
    digito= num % 10
    num=trunc(num/10)
    numInver=numInver*10+digito
   
print("El número invertido es: ", numInver)
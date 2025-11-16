## TP-9 RECURSIVIDAD

# 1- Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
#función para calcular y mostrar en pantalla el factorial de todos los números enteros 
#entre 1 y el número que indique el usuario

def factorial_num(num):
    if num <= 0:
        return 1
    else:
       return num * factorial_num( num-1)


num_usuario = int(input("Ingrese un número para calcular el factorial de los numeros hasta el indicado: "))

if num_usuario <=0:
    print(1)  
else:
    for i in range(1,num_usuario+1):
        print(f"El factorial de {i} es: {factorial_num(i)}")

# 2- Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
#especifique. 

def fibionacci_recur(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibionacci_recur(posicion-1) + fibionacci_recur(posicion-2)
    

num_usuario=int(input("Ingrese un número para calcular la serie de Fibionacci: "))

print(f"La serie de Fibionacci en la posicion {num_usuario} es : {fibionacci_recur(num_usuario)}")

for i in range(1,num_usuario+1):
    print(f"La serie de Fibionacci de {i} es : {fibionacci_recur(i)}")


# 3- Crea una función recursiva que calcule la potencia de un número base elevado a un 
#exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
#algoritmo general. 

def funcion_recur_potencia(base,exponente):
    if exponente == 0:
        return 1
    else: 
        return base * funcion_recur_potencia(base, exponente - 1)

# 4- Crear una función recursiva en Python que reciba un número entero positivo en base 
#decimal y devuelva su representación en binario como una cadena de texto. 

def dec_a_binario(num):
    if num == 0 :
        return "0"
    if num == 1:
        return "1"
    return dec_a_binario(num//2)+str(num%2)
       
num_usuario=int(input("Ingrese un número entero: "))
print(f"{dec_a_binario(num_usuario)}")

# 5- Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
#lo es. 

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0]==palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False


palabra_user=input("Ingrese una palabra para ver si es palídromo: ")
print(es_palindromo(palabra_user))

# 6- Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
#número entero positivo y devuelva la suma de todos sus dígitos. 

def suma_digitos(num):
    
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return num%10 + suma_digitos(num//10)

num_user=int(input("Ingrese un número para contar los dígitos: "))    
print(suma_digitos(num_user))

# 7- Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloc#a n 
#bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
#último nivel con un solo bloque. 
 
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
#nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
#pirámide.

def contar_bloques(bloques):
    if bloques <= 0:
        return 0
    elif bloques == 1:
        return 1
    else:
        return bloques + contar_bloques(bloques-1)
    
bloques_user = int(input("Ingrese el número de bloques: "))
print(contar_bloques(bloques_user))  

# 8- Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
#aparece ese dígito dentro del número.  

def contar_digito(numero, digito):  
    if numero == 0:
        return 0
    ultimo_digito = numero % 10

    if ultimo_digito == digito:
        return 1 + contar_digito(numero//10,digito)
    else:
        return contar_digito(numero//10,digito)
    
num_user=int(input("Ingrese un número para contar los dígitos repetidos "))  
digito_user= int(input("Ingrese el dígito a identificar: "))  
print(contar_digito(num_user,digito_user))    
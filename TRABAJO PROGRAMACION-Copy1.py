#!/usr/bin/env python
# coding: utf-8

# In[4]:


#ejercicio 1
name= input("ingrese nombre: ")
age= input("ingrese edad: ")

print("nombre:", name, "y su edad es", age)


# In[6]:


#ejercicio 2

import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = float(input("Ingrese el radio del círculo: "))
area_del_circulo = calcular_area_circulo(radio)
print("El área del círculo es:", area_del_circulo)


# In[12]:


#ejercicio 3

import random

numero_aleatorio = random.randint(1, 100)
print("Número entero aleatorio:", numero_aleatorio)


# In[13]:


#ejercicio 4

def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero_ingresado = int(input("Ingrese un número: "))

resultado = es_par_o_impar(numero_ingresado)

print(f"El número {numero_ingresado} es {resultado}.")


# In[1]:


#ejercicio 5

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f} grados Fahrenheit son {celsius:.2f} grados Celsius.")
    except ValueError:
        print("no es valido.")

fahrenheit_to_celsius()


# In[ ]:


#ejercicio 6

def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius


temperatura_fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
temperatura_celsius = fahrenheit_a_celsius(temperatura_fahrenheit)
print("La temperatura en grados Celsius es:", temperatura_celsius)


# In[15]:


#ejercicio 7

def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso:
lista_numeros = [9, 2, 56, 3, 5]
suma_total = suma_lista(lista_numeros)
print("La suma de los números en la lista es:", suma_total)


# In[16]:


#ejercicio 8

def maximo_minimo(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

lista_numeros = [7, 1, 7, 2, 9, 3]
maximo_numero, minimo_numero = maximo_minimo(lista_numeros)

print("El número más grande es:", maximo_numero)
print("El número más pequeño es:", minimo_numero)


# In[18]:


#ejercicio 9

def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

lista_ori = [8, 12, 3, 42, 5]
lista_i = invertir_lista(lista_ori)

print("Lista normal:", lista_original)
print("Lista invertida:", lista_i)


# In[30]:


#ejercicio 1

def factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero_dado = int(input("Ingrese un número entero : "))
resultado_factorial = factorial(numero_dado)
print("El factorial de", numero_dado, "es:", resultado_factorial)


# In[23]:


#ejercicio 11

def generar_lista():
    lista = []
    for numero in range(2, 101, 2):
        lista.append(numero)
    return lista

lista_numeros_pares = generar_lista_numeros_pares()

print("Lista de números pares entre 1 y 100:")
print(lista_numeros_pares)


# In[24]:


#ejercicio 12

for numero in range(1, 11):
    print(numero)


# In[25]:


#ejercicio 13

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma= numero1 + numero2
resta= numero1 - numero2
multiplicacion= numero1 * numero2
division= numero1 / numero2

print("la suma de los numeros da: ", suma)
print("la resta de los numeros da: ", resta)
print("la multiplicacion de los numeros da:", multiplicacion)
print("la division de los numeros da:", division)


# In[27]:


#ejercicio 14

def media_aritmetica(lista):
    suma = sum(lista)
    cantidad_elementos = len(lista)
    media = suma / cantidad_elementos
    return media

# Ejemplo de uso:
lista_numeros = [18, 20, 38, 20, 50]
media_aritmetica = media_aritmetica(lista_numeros)
print("La media aritmética es:", media_aritmetica)


# In[ ]:


#ejercicio 15
def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

def main():
    texto = input("Ingresa una cadena de texto: ")
    if es_palindromo(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")

if __name__ == "__main__":
    main()


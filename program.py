# programa.py
# Programa base para el taller colaborativo

def saludar():
 print("Hola, este es el programa base del taller")

saludar()
# 1. Definimos la función primero
def suma(a, b):
    return a + b

# 2. Pedimos los datos al usuario (Aquí se definen 'valor1' y 'valor2')
valor1 = input("Ingrese el primer valor: ")
valor2 = input("Ingrese el segundo valor: ")

# 3. Ahora sí podemos usarlas porque ya existen
print("El primer valor ingresado es:", valor1)
print("El segundo valor ingresado es:", valor2)

# 4. Llamamos a la función convirtiendo a entero (int)
print("La suma es:", suma(int(valor1), int(valor2)))
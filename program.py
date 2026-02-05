# programa.py
# Programa base para el taller colaborativo

def mensaje_de_gloria():
    autor = "Gloria Jaramillo"
    mensaje = "¡Aquí hice mi contribución!"
    
    print(f"Hola, soy {autor} y {mensaje}")
 
if __name__ == "__main__":
    mensaje_de_gloria()

def saludar():
 print("Hola, este es el programa base del taller")
 #editado por Raymer
 print("Esta prueba ha sido realizada por Angie De Gracia")
 #Editado por GloriaJAQ
 print("Hola, soy GloriaJAQ y ¡Aquí hice mi contribución!")

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
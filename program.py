# Autor: John Miró
# Fecha: 2026
# Descripción: Mejora del programa base agregando interacción con el usuario

def saludar(nombre):
    return f"Hola {nombre}, bienvenido al taller de Git y GitHub"

usuario = input("Ingrese su nombre: ")
print(saludar(usuario))

# Registro de Estudiantes
# Programa sencillo que usa una LISTA para guardar nombres de estudiantes.

estudiantes = []  # lista vacía donde se guardarán los nombres

# Agregar estudiantes a la lista
estudiantes.append("Jesús")
estudiantes.append("Pedro")
estudiantes.append("Pablo")

# También se puede pedir un nombre al usuario y agregarlo
nuevo = input("Escribe el nombre de un nuevo estudiante: ")
estudiantes.append(nuevo)

# Mostrar todos los estudiantes registrados
print("\nLista de estudiantes registrados:")
for nombre in estudiantes:
    print("-", nombre)

# Operación adicional: buscar un estudiante en la lista
buscar = input("\nEscribe un nombre para buscar en la lista: ")
if buscar in estudiantes:
    print(f"'{buscar}' sí está registrado en la lista.")
else:
    print(f"'{buscar}' no está registrado en la lista.")
